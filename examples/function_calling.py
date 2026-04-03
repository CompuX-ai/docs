"""CompuX Function Calling — Tool use with the OpenAI-compatible API."""

import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_compute_price",
            "description": "Get the current price for a GPU instance type",
            "parameters": {
                "type": "object",
                "properties": {
                    "gpu_type": {
                        "type": "string",
                        "description": "GPU type, e.g. H100, A100, L40S",
                    },
                    "provider": {
                        "type": "string",
                        "description": "Cloud provider, e.g. aws, gcp, lambda",
                    },
                },
                "required": ["gpu_type"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_credits",
            "description": "Calculate how many compute credits a dollar amount converts to",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount_usd": {
                        "type": "number",
                        "description": "Dollar amount to convert",
                    },
                    "plan": {
                        "type": "string",
                        "enum": ["starter", "growth", "scale", "enterprise"],
                        "description": "CompuX plan tier",
                    },
                },
                "required": ["amount_usd"],
            },
        },
    },
]


def get_compute_price(gpu_type: str, provider: str = "any") -> dict:
    """Mock implementation — replace with real API call."""
    prices = {
        "H100": {"aws": 4.50, "gcp": 4.20, "lambda": 2.49},
        "A100": {"aws": 3.10, "gcp": 2.95, "lambda": 1.29},
        "L40S": {"aws": 1.80, "gcp": 1.70, "lambda": 0.99},
    }
    if gpu_type in prices:
        if provider in prices[gpu_type]:
            return {"gpu_type": gpu_type, "provider": provider, "price_per_hour": prices[gpu_type][provider]}
        return {"gpu_type": gpu_type, "prices": prices[gpu_type]}
    return {"error": f"Unknown GPU type: {gpu_type}"}


def calculate_credits(amount_usd: float, plan: str = "starter") -> dict:
    """Calculate credit conversion with financing multiplier."""
    multipliers = {"starter": 1.0, "growth": 1.25, "scale": 1.35, "enterprise": 1.50}
    multiplier = multipliers.get(plan, 1.0)
    return {
        "amount_usd": amount_usd,
        "plan": plan,
        "multiplier": multiplier,
        "credits": amount_usd * multiplier,
    }


# Available functions
available_functions = {
    "get_compute_price": get_compute_price,
    "calculate_credits": calculate_credits,
}


def run_conversation(user_message: str) -> str:
    """Run a conversation with function calling."""
    messages = [{"role": "user", "content": user_message}]

    # First call — model decides which tools to use
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message

    # If the model wants to call functions
    if message.tool_calls:
        messages.append(message)

        for tool_call in message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            # Execute the function
            fn_response = available_functions[fn_name](**fn_args)

            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "content": json.dumps(fn_response),
            })

        # Second call — model generates final response with function results
        final = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        return final.choices[0].message.content

    return message.content


if __name__ == "__main__":
    print(run_conversation("How much would $10,000 get me in credits on the Scale plan?"))
    print()
    print(run_conversation("Compare H100 prices across providers"))