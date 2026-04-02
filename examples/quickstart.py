"""CompuX Quickstart — Drop-in OpenAI replacement with 25-50% cost savings."""

from openai import OpenAI

# Initialize with CompuX endpoint
client = OpenAI(
    api_key="YOUR_COMPUX_API_KEY",  # Get yours at app.compux.ai
    base_url="https://api.compux.ai/v1",
)

# Same OpenAI SDK, same API — just cheaper
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain compute credits in one sentence."},
    ],
)

print(response.choices[0].message.content)