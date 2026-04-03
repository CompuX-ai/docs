"""CompuX Streaming Example — Real-time token streaming via OpenAI-compatible API.

Setup: export COMPUX_API_KEY="cpx_live_..."
       pip install openai
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is AI compute financing?"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()  # newline at end