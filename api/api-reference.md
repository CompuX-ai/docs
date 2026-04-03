# CompuX API Reference

CompuX provides an OpenAI-compatible REST API for chat completions, embeddings, and model management. Every endpoint follows the OpenAI specification — existing SDKs work with zero code changes beyond swapping the base URL and API key.

**Key Takeaways:**

* **Base URL** — `https://api.compux.ai/v1` for all API requests.
* **OpenAI-Compatible** — Same request/response format as OpenAI. Use the official OpenAI SDK in Python, TypeScript, Go, or any language.
* **Multi-Provider** — A single API key routes to OpenAI, Anthropic, Google, Mistral, Meta, and open-source models.
* **Streaming** — Full SSE streaming support for chat completions.
* **Cost Savings** — 25-50% cheaper than direct provider pricing through [compute credit financing](../concepts/compute-credits.md).

## Base URL

All API requests use:

```
https://api.compux.ai/v1
```

## Authentication

Every request requires a Bearer token in the `Authorization` header:

```
Authorization: Bearer YOUR_COMPUX_API_KEY
```

Get your API key at [app.compux.ai](https://app.compux.ai). See the [Authentication Guide](authentication.md) for details on key management, scopes, and rotation.

## Endpoints

### POST /v1/chat/completions

Generate a chat completion. Supports all OpenAI chat completion parameters.

**Request:**

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Explain compute credits."}
    ],
    "temperature": 0.7,
    "max_tokens": 1024,
    "stream": false
  }'
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Model identifier. See [Available Models](models.md). |
| `messages` | array | Yes | Array of message objects with `role` and `content`. |
| `temperature` | float | No | Sampling temperature (0.0-2.0). Default: 1.0. |
| `max_tokens` | integer | No | Maximum tokens to generate. Model-dependent default. |
| `stream` | boolean | No | Enable SSE streaming. Default: false. |
| `top_p` | float | No | Nucleus sampling (0.0-1.0). Default: 1.0. |
| `n` | integer | No | Number of completions to generate. Default: 1. |
| `stop` | string/array | No | Stop sequence(s). Up to 4 sequences. |
| `presence_penalty` | float | No | Penalize new tokens by presence (-2.0 to 2.0). Default: 0. |
| `frequency_penalty` | float | No | Penalize new tokens by frequency (-2.0 to 2.0). Default: 0. |
| `tools` | array | No | Function/tool definitions for function calling. |
| `tool_choice` | string/object | No | Control tool selection: "auto", "none", or specific tool. |
| `response_format` | object | No | Force JSON output: `{"type": "json_object"}`. |
| `seed` | integer | No | Deterministic sampling seed. |

**Response (200 OK):**

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1711234567,
  "model": "gpt-4o",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Compute credits are standardized units of cloud computing resources..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 85,
    "total_tokens": 109
  },
  "x_compux": {
    "provider": "openai",
    "credits_used": 0.00218,
    "credits_remaining": 12497.42
  }
}
```

The `x_compux` field is a CompuX extension showing provider routing, credit usage, and remaining balance.

**Streaming Response (SSE):**

When `stream: true`, the API returns Server-Sent Events:

```
data: {"id":"chatcmpl-abc123","object":"chat.completion.chunk","choices":[{"delta":{"role":"assistant"},"index":0}]}

data: {"id":"chatcmpl-abc123","object":"chat.completion.chunk","choices":[{"delta":{"content":"Compute"},"index":0}]}

data: {"id":"chatcmpl-abc123","object":"chat.completion.chunk","choices":[{"delta":{"content":" credits"},"index":0}]}

data: [DONE]
```

### POST /v1/embeddings

Generate vector embeddings for text input.

```bash
curl https://api.compux.ai/v1/embeddings \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-3-small",
    "input": "AI compute credit marketplace"
  }'
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Embedding model identifier. |
| `input` | string/array | Yes | Text to embed. String or array of strings. |
| `encoding_format` | string | No | "float" (default) or "base64". |
| `dimensions` | integer | No | Output dimensions (model-dependent). |

**Response (200 OK):**

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [0.0023, -0.0091, 0.0156, ...],
      "index": 0
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
```

### GET /v1/models

List all available models on your account.

```bash
curl https://api.compux.ai/v1/models \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

**Response (200 OK):**

```json
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4o",
      "object": "model",
      "created": 1706745600,
      "owned_by": "openai",
      "x_compux": {
        "provider": "openai",
        "supports_streaming": true,
        "supports_function_calling": true,
        "supports_vision": true,
        "context_window": 128000,
        "cost_per_1k_input": 0.0025,
        "cost_per_1k_output": 0.01
      }
    }
  ]
}
```

### GET /v1/models/{model_id}

Get details for a specific model.

```bash
curl https://api.compux.ai/v1/models/gpt-4o \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

### GET /v1/account/credits

CompuX extension — check your credit balance and usage.

```bash
curl https://api.compux.ai/v1/account/credits \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

**Response (200 OK):**

```json
{
  "total_credits": 15000.00,
  "used_credits": 2502.58,
  "remaining_credits": 12497.42,
  "blocked_credits": 0.00,
  "credits_expiry": "2027-04-01T00:00:00Z",
  "plan": "startup-series-a",
  "financing_multiplier": 1.35
}
```

### GET /v1/account/usage

CompuX extension — detailed usage breakdown by model and provider.

```bash
curl https://api.compux.ai/v1/account/usage?start_date=2026-04-01&end_date=2026-04-03 \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

**Response (200 OK):**

```json
{
  "start_date": "2026-04-01",
  "end_date": "2026-04-03",
  "total_credits": 47.82,
  "total_requests": 12450,
  "by_model": [
    {
      "model": "gpt-4o",
      "provider": "openai",
      "requests": 8200,
      "input_tokens": 4100000,
      "output_tokens": 1230000,
      "credits": 35.10
    },
    {
      "model": "claude-sonnet-4-20250514",
      "provider": "anthropic",
      "requests": 4250,
      "input_tokens": 2125000,
      "output_tokens": 637500,
      "credits": 12.72
    }
  ]
}
```

## SDK Examples

### Python (OpenAI SDK)

```bash
pip install openai
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

### TypeScript / Node.js (OpenAI SDK)

```bash
npm install openai
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-4o",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(response.choices[0].message.content);
```

### Go

```go
package main

import (
    "context"
    "fmt"
    "os"
    openai "github.com/sashabaranov/go-openai"
)

func main() {
    config := openai.DefaultConfig(os.Getenv("COMPUX_API_KEY"))
    config.BaseURL = "https://api.compux.ai/v1"
    client := openai.NewClientWithConfig(config)

    resp, err := client.CreateChatCompletion(
        context.Background(),
        openai.ChatCompletionRequest{
            Model: openai.GPT4o,
            Messages: []openai.ChatCompletionMessage{
                {Role: openai.ChatMessageRoleUser, Content: "Hello!"},
            },
        },
    )
    if err != nil {
        panic(err)
    }
    fmt.Println(resp.Choices[0].Message.Content)
}
```

### cURL

```bash
export COMPUX_API_KEY="your-key-here"

curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Pagination

List endpoints support cursor-based pagination:

```bash
curl "https://api.compux.ai/v1/models?limit=20&after=model_abc123" \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | integer | Number of results per page (1-100, default 20). |
| `after` | string | Cursor for next page (from previous response). |

## Request Headers

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | `Bearer YOUR_API_KEY` |
| `Content-Type` | Yes (POST) | `application/json` |
| `X-CompuX-Provider` | No | Force specific provider: `openai`, `anthropic`, `google`, `mistral`. |
| `X-CompuX-Budget-Limit` | No | Max credits for this request. Returns 402 if exceeded. |
| `X-CompuX-Request-ID` | No | Custom request ID for tracking and debugging. |

## Related Resources

- [Available Models](models.md) — Full model list with capabilities and pricing
- [Authentication](authentication.md) — API key management, scopes, and rotation
- [Error Handling](errors.md) — HTTP status codes, error schema, and retry logic
- [Rate Limits](rate-limits.md) — Request and token limits by plan
- [Pricing](pricing.md) — Credit costs, conversion rates, and calculators
- [Compute Credits](../concepts/compute-credits.md) — How the credit system works
- [OpenAI-Compatible API FAQ](../faq/openai-compatible-api.md) — Common integration questions