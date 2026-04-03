# Error Handling

CompuX returns standard HTTP status codes and structured JSON error responses. Every error includes a machine-readable `code`, a human-readable `message`, and the error `type` for programmatic handling.

**Key Takeaways:**

* **Standard HTTP Codes** — 4xx for client errors, 5xx for server errors.
* **Structured Responses** — Every error returns `{error: {message, type, code}}` JSON.
* **Retry-Safe** — 429 and 5xx errors are safe to retry with exponential backoff.
* **Provider Transparency** — Errors include which provider failed when relevant.
* **OpenAI-Compatible** — Error format matches OpenAI's specification for SDK compatibility.

## Error Response Format

All errors return this structure:

```json
{
  "error": {
    "message": "Human-readable description of what went wrong.",
    "type": "error_category",
    "code": "machine_readable_code",
    "param": "field_name"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `message` | string | Description of the error. Safe to display to users. |
| `type` | string | Error category for programmatic handling. |
| `code` | string | Specific error code. |
| `param` | string | Which parameter caused the error (when applicable). |

## HTTP Status Codes

### Client Errors (4xx)

| Status | Type | Code | Description |
|--------|------|------|-------------|
| **400** | `invalid_request_error` | `invalid_request` | Malformed request body or missing required fields. |
| **400** | `invalid_request_error` | `invalid_model` | Requested model does not exist or is not available. |
| **400** | `invalid_request_error` | `context_length_exceeded` | Input exceeds model's context window. |
| **400** | `invalid_request_error` | `invalid_messages` | Messages array is empty or incorrectly formatted. |
| **401** | `authentication_error` | `invalid_api_key` | API key is missing, invalid, or revoked. |
| **401** | `authentication_error` | `expired_api_key` | API key has passed its expiration date. |
| **403** | `permission_error` | `insufficient_scope` | API key lacks the required scope for this endpoint. |
| **403** | `permission_error` | `ip_not_allowed` | Request IP is not on the key's allowlist. |
| **402** | `billing_error` | `insufficient_credits` | Account has no remaining [compute credits](../concepts/compute-credits.md). |
| **402** | `billing_error` | `budget_exceeded` | Key's monthly credit limit reached. |
| **402** | `billing_error` | `credits_blocked` | Credits are frozen by lender ([blockable credits](../concepts/blockable-credits.md)). |
| **404** | `not_found_error` | `model_not_found` | Model ID not recognized. |
| **404** | `not_found_error` | `endpoint_not_found` | URL path does not match any endpoint. |
| **413** | `invalid_request_error` | `request_too_large` | Request body exceeds 10MB limit. |
| **422** | `invalid_request_error` | `invalid_tool_definition` | Tool/function schema is malformed. |
| **429** | `rate_limit_error` | `rate_limit_exceeded` | Too many requests. See [Rate Limits](rate-limits.md). |
| **429** | `rate_limit_error` | `token_limit_exceeded` | Token usage limit reached for current window. |

### Server Errors (5xx)

| Status | Type | Code | Description |
|--------|------|------|-------------|
| **500** | `server_error` | `internal_error` | Unexpected server error. Safe to retry. |
| **502** | `server_error` | `provider_error` | Upstream provider returned an error. |
| **503** | `server_error` | `provider_unavailable` | Upstream provider is temporarily unavailable. |
| **503** | `server_error` | `overloaded` | CompuX is experiencing high load. Retry with backoff. |
| **504** | `server_error` | `provider_timeout` | Upstream provider did not respond in time. |

## Error Examples

### Invalid API Key (401)

```json
{
  "error": {
    "message": "Invalid API key provided. You can find your API key at app.compux.ai/settings/api-keys.",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

### Insufficient Credits (402)

```json
{
  "error": {
    "message": "You have insufficient credits to complete this request. Your balance is 0.42 credits. This request requires approximately 2.50 credits. Top up at app.compux.ai/billing.",
    "type": "billing_error",
    "code": "insufficient_credits"
  }
}
```

### Context Length Exceeded (400)

```json
{
  "error": {
    "message": "This request contains 135,000 tokens, which exceeds the maximum context length of 128,000 tokens for model gpt-4o. Try reducing your input or using a model with a larger context window (e.g., gemini-2.5-pro with 1M tokens).",
    "type": "invalid_request_error",
    "code": "context_length_exceeded",
    "param": "messages"
  }
}
```

### Rate Limit Exceeded (429)

```json
{
  "error": {
    "message": "Rate limit exceeded. You are sending requests too quickly. Please slow down. Limit: 500 RPM. Current: 523 RPM. Retry after 3 seconds.",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

Response includes a `Retry-After` header:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 3
X-RateLimit-Limit-Requests: 500
X-RateLimit-Remaining-Requests: 0
X-RateLimit-Reset-Requests: 2026-04-03T12:00:03Z
```

### Provider Error (502)

```json
{
  "error": {
    "message": "The upstream provider (openai) returned an error: 'Service temporarily unavailable'. CompuX will automatically retry with an alternative provider if available.",
    "type": "server_error",
    "code": "provider_error"
  }
}
```

## Retry Strategy

### Which Errors to Retry

| Error Code | Retry? | Strategy |
|------------|--------|----------|
| `rate_limit_exceeded` | Yes | Wait for `Retry-After` header value |
| `token_limit_exceeded` | Yes | Wait for rate limit window reset |
| `internal_error` (500) | Yes | Exponential backoff |
| `provider_error` (502) | Yes | Immediate retry (different provider may be selected) |
| `provider_unavailable` (503) | Yes | Exponential backoff |
| `provider_timeout` (504) | Yes | Exponential backoff with longer timeout |
| `overloaded` (503) | Yes | Exponential backoff, minimum 5s |
| `invalid_api_key` (401) | No | Fix the API key |
| `insufficient_credits` (402) | No | Top up credits |
| `invalid_request` (400) | No | Fix the request |

### Exponential Backoff (Python)

```python
import time
from openai import OpenAI, RateLimitError, APIStatusError

client = OpenAI(
    api_key="YOUR_COMPUX_API_KEY",
    base_url="https://api.compux.ai/v1",
)

def chat_with_retry(messages, model="gpt-4o", max_retries=5):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model=model,
                messages=messages,
            )
        except RateLimitError as e:
            retry_after = int(e.response.headers.get("Retry-After", 2 ** attempt))
            print(f"Rate limited. Retrying in {retry_after}s...")
            time.sleep(retry_after)
        except APIStatusError as e:
            if e.status_code >= 500:
                wait = min(2 ** attempt, 30)
                print(f"Server error {e.status_code}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise  # Don't retry 4xx errors (except 429)
    raise Exception(f"Failed after {max_retries} retries")
```

### Exponential Backoff (TypeScript)

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});

async function chatWithRetry(
  messages: OpenAI.ChatCompletionMessageParam[],
  model = "gpt-4o",
  maxRetries = 5
): Promise<OpenAI.ChatCompletion> {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await client.chat.completions.create({ model, messages });
    } catch (error) {
      if (error instanceof OpenAI.RateLimitError) {
        const retryAfter = Number(error.headers?.["retry-after"]) || 2 ** attempt;
        console.log(`Rate limited. Retrying in ${retryAfter}s...`);
        await new Promise((r) => setTimeout(r, retryAfter * 1000));
      } else if (error instanceof OpenAI.APIError && error.status >= 500) {
        const wait = Math.min(2 ** attempt, 30);
        console.log(`Server error ${error.status}. Retrying in ${wait}s...`);
        await new Promise((r) => setTimeout(r, wait * 1000));
      } else {
        throw error;
      }
    }
  }
  throw new Error(`Failed after ${maxRetries} retries`);
}
```

## Rate Limit Headers

Every response includes rate limit information:

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit-Requests` | Maximum requests per minute for your plan |
| `X-RateLimit-Limit-Tokens` | Maximum tokens per minute for your plan |
| `X-RateLimit-Remaining-Requests` | Requests remaining in current window |
| `X-RateLimit-Remaining-Tokens` | Tokens remaining in current window |
| `X-RateLimit-Reset-Requests` | When the request limit resets (ISO 8601) |
| `X-RateLimit-Reset-Tokens` | When the token limit resets (ISO 8601) |
| `Retry-After` | Seconds to wait before retrying (only on 429) |

## Common Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `invalid_api_key` on every request | Key not set or wrong prefix | Check `echo $COMPUX_API_KEY` starts with `cpx_live_` or `cpx_test_` |
| `insufficient_credits` suddenly | Credits depleted or blocked | Check balance at `GET /v1/account/credits` or dashboard |
| `context_length_exceeded` | Input too long | Truncate input or switch to a larger context model |
| `rate_limit_exceeded` spike | Burst traffic | Implement retry with backoff. Consider upgrading plan |
| `provider_error` intermittent | Upstream provider issue | Usually auto-resolves. CompuX may route to alternate provider |
| `invalid_model` | Typo in model name | Check `GET /v1/models` for exact IDs |

## Related Resources

- [API Reference](api-reference.md) — Endpoint documentation
- [Rate Limits](rate-limits.md) — Detailed limits by plan
- [Authentication](authentication.md) — API key management
- [Available Models](models.md) — Valid model identifiers