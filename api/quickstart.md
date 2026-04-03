# Quickstart Guide

Get running with the CompuX API in under 5 minutes. CompuX is a drop-in OpenAI replacement — if you have used the OpenAI SDK, you already know how to use CompuX.

**Key Takeaways:**

* **5-Minute Setup** — Sign up, get a key, make your first request.
* **Zero Code Changes** — Use the OpenAI SDK you already have. Just change 2 lines.
* **Any Language** — Python, TypeScript, Go, Ruby, or plain cURL.
* **Free Tier** — 5 credits free to test. No credit card required.
* **Sandbox Available** — Test with `cpx_test_` keys at no cost.

## Step 1: Get Your API Key

1. Go to [app.compux.ai/register](https://app.compux.ai/register)
2. Create an account (email or GitHub SSO)
3. Navigate to **Settings → API Keys**
4. Click **Create Key**
5. Copy the key — it starts with `cpx_live_` or `cpx_test_`

Set it as an environment variable:

```bash
export COMPUX_API_KEY="cpx_live_your_key_here"
```

## Step 2: Install the SDK

CompuX works with the standard OpenAI SDK. No custom package needed.

### Python

```bash
pip install openai
```

### TypeScript / Node.js

```bash
npm install openai
```

### Go

```bash
go get github.com/sashabaranov/go-openai
```

## Step 3: Make Your First Request

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are compute credits?"},
    ],
)

print(response.choices[0].message.content)
```

### TypeScript

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});

async function main() {
  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "What are compute credits?" },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### cURL

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What are compute credits?"}
    ]
  }'
```

## Step 4: Try Streaming

Get tokens as they are generated for real-time UIs:

```python
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explain AI compute financing in 3 sentences."}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
```

## Step 5: Try Different Models

Switch between providers by changing one parameter:

```python
# OpenAI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}],
)

# Anthropic
response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Hello!"}],
)

# Google
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "Hello!"}],
)

# Meta (open-source)
response = client.chat.completions.create(
    model="llama-4-maverick",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

All models use the same SDK, same format, same API key. See [Available Models](models.md) for the complete list.

## Step 6: Check Your Credit Balance

```python
import requests
import os

headers = {"Authorization": f"Bearer {os.environ['COMPUX_API_KEY']}"}
r = requests.get("https://api.compux.ai/v1/account/credits", headers=headers)
balance = r.json()

print(f"Remaining credits: {balance['remaining_credits']}")
print(f"Financing multiplier: {balance['financing_multiplier']}x")
```

## Migrating from OpenAI

If you already use the OpenAI API, migration is two lines:

```python
# Before
client = OpenAI(api_key="sk-...")

# After
client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],  # Line 1: new key
    base_url="https://api.compux.ai/v1",   # Line 2: new URL
)

# Everything else stays exactly the same
```

Your existing code, parameters, error handling, and streaming all work unchanged. CompuX passes through the same request/response format.

## Using with Frameworks

### LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

response = llm.invoke("What is a token operator?")
```

### LlamaIndex

```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model="gpt-4o",
    api_key=os.environ["COMPUX_API_KEY"],
    api_base="https://api.compux.ai/v1",
)
```

### Vercel AI SDK

```typescript
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const compux = createOpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});

const { text } = await generateText({
  model: compux("gpt-4o"),
  prompt: "What are compute credits?",
});
```

### Claude Code

Add to your Claude Code config (`~/.claude.json` or project settings):

```json
{
  "apiProvider": "custom",
  "customApiUrl": "https://api.compux.ai/v1",
  "customApiKey": "cpx_live_your_key_here"
}
```

## What's Next?

- [API Reference](api-reference.md) — Full endpoint documentation
- [Available Models](models.md) — 100+ models with pricing
- [Error Handling](errors.md) — Handle errors gracefully
- [Rate Limits](rate-limits.md) — Understand your limits
- [Pricing](pricing.md) — Plans, credits, and financing multipliers
- [Authentication](authentication.md) — Key management and security
- [Function Calling Example](../examples/function_calling.py) — Tool use with CompuX
- [Async Example](../examples/async_client.py) — High-throughput async patterns