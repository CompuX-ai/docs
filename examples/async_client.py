"""CompuX Async Client — High-throughput parallel requests with rate limit awareness."""

import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)


async def chat(message: str, model: str = "gpt-4o-mini") -> str:
    """Send a single chat request asynchronously."""
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content


async def batch_chat(messages: list[str], model: str = "gpt-4o-mini", concurrency: int = 10) -> list[str]:
    """Process multiple messages with controlled concurrency."""
    semaphore = asyncio.Semaphore(concurrency)

    async def limited_chat(msg: str) -> str:
        async with semaphore:
            return await chat(msg, model)

    tasks = [limited_chat(msg) for msg in messages]
    return await asyncio.gather(*tasks)


async def main():
    # Single request
    result = await chat("What is a compute credit?")
    print(f"Single: {result[:100]}...")

    # Batch of 20 requests with concurrency limit of 5
    prompts = [f"Explain concept #{i} of AI compute" for i in range(20)]
    results = await batch_chat(prompts, concurrency=5)
    print(f"\nBatch: {len(results)} responses received")
    for i, r in enumerate(results[:3]):
        print(f"  [{i}] {r[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())