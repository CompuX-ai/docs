# Authentication

CompuX uses API keys for authentication. Every request must include a valid API key in the `Authorization` header. Keys are scoped to your organization and can be restricted by permissions, IP allowlists, and expiration dates.

**Key Takeaways:**

* **Bearer Token** — All requests use `Authorization: Bearer YOUR_API_KEY`.
* **Create at app.compux.ai** — Generate and manage keys in the [CompuX Dashboard](https://app.compux.ai/settings/api-keys).
* **Scoped Permissions** — Keys can be restricted to specific models, endpoints, or credit budgets.
* **Rotate Regularly** — Create new keys and revoke old ones without downtime.
* **Never Hardcode** — Use environment variables or secret managers. Never commit keys to version control.

## Getting Your API Key

1. Sign up at [app.compux.ai/register](https://app.compux.ai/register)
2. Complete the onboarding process (2-3 business days for financing; instant for API-only access)
3. Go to **Settings → API Keys**
4. Click **Create Key**
5. Copy the key immediately — it will not be shown again

```
cpx_live_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

CompuX API keys start with `cpx_live_` (production) or `cpx_test_` (sandbox).

## Using Your API Key

### Environment Variable (Recommended)

```bash
export COMPUX_API_KEY="cpx_live_a1b2c3d4e5f6..."
```

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)
```

### TypeScript / Node.js

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});
```

### cURL

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "messages": [{"role": "user", "content": "Hello"}]}'
```

## API Key Types

| Key Type | Prefix | Purpose | Rate Limits |
|----------|--------|---------|-------------|
| **Production** | `cpx_live_` | Live API requests, billed to your account | Full plan limits |
| **Sandbox** | `cpx_test_` | Testing and development, no credit charges | 100 RPM, 10K TPM |
| **Restricted** | `cpx_live_` | Production with scoped permissions | Custom |

## Key Scopes and Permissions

When creating a key, you can restrict its permissions:

| Scope | Description |
|-------|-------------|
| `chat.completions` | Access to `/v1/chat/completions` endpoint |
| `embeddings` | Access to `/v1/embeddings` endpoint |
| `models.read` | Access to `/v1/models` (list and get) |
| `account.read` | Access to `/v1/account/credits` and `/v1/account/usage` |
| `account.manage` | Manage API keys and account settings |
| `*` | Full access (default) |

Example: Create a key that can only make chat completions with GPT-4o:

```json
{
  "name": "production-chatbot",
  "scopes": ["chat.completions"],
  "allowed_models": ["gpt-4o", "gpt-4o-mini"],
  "monthly_credit_limit": 500.00,
  "expires_at": "2027-01-01T00:00:00Z"
}
```

## Key Rotation

Rotate keys without downtime by running two keys simultaneously:

1. **Create a new key** in the dashboard
2. **Deploy the new key** to your application
3. **Verify requests** succeed with the new key
4. **Revoke the old key** once fully migrated

Both keys work simultaneously during migration. There is no limit on the number of active keys per account.

## IP Allowlisting

Restrict API key usage to specific IP addresses or CIDR ranges:

```json
{
  "name": "production-server",
  "allowed_ips": [
    "203.0.113.0/24",
    "198.51.100.42"
  ]
}
```

Requests from non-allowed IPs receive a `403 Forbidden` response.

## Credit Budget Limits

Set a maximum credit spend per key to prevent runaway costs:

```json
{
  "name": "dev-team-key",
  "monthly_credit_limit": 100.00,
  "alert_threshold": 80.00
}
```

When the limit is reached, the key returns `402 Payment Required` until the next billing cycle or the limit is increased.

## Sandbox Environment

Use sandbox keys for development and testing:

| Feature | Production (`cpx_live_`) | Sandbox (`cpx_test_`) |
|---------|--------------------------|----------------------|
| Billing | Real credits charged | No charges |
| Models | All available | All available |
| Rate limits | Full plan limits | 100 RPM, 10K TPM |
| Responses | Live model output | Live model output |
| Data | Logged for billing | Logged for debugging |

Sandbox keys use the same base URL:

```python
client = OpenAI(
    api_key="cpx_test_...",  # Sandbox key
    base_url="https://api.compux.ai/v1",
)
```

## Security Best Practices

1. **Never hardcode keys** — Use environment variables, `.env` files, or secret managers (AWS Secrets Manager, HashiCorp Vault, 1Password)
2. **Never commit keys** — Add `.env` to `.gitignore`. Use pre-commit hooks to scan for leaked secrets
3. **Use scoped keys** — Create separate keys per application/team with minimum required permissions
4. **Set expiration dates** — Keys should expire and be rotated at least quarterly
5. **Monitor usage** — Check the dashboard for unexpected activity. Set up alerts
6. **Revoke immediately** — If a key is compromised, revoke it in the dashboard. Create a new one

## Verifying Your Key

Test that your key works:

```bash
curl https://api.compux.ai/v1/models \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

**Success (200):** Returns list of available models.

**Invalid key (401):**
```json
{
  "error": {
    "message": "Invalid API key. Check your key at app.compux.ai/settings/api-keys",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

## Related Resources

- [API Reference](api-reference.md) — Full endpoint documentation
- [Error Handling](errors.md) — Authentication error codes
- [Rate Limits](rate-limits.md) — Limits by key type and plan
- [Getting Started FAQ](../faq/getting-started-compux.md) — Onboarding and account setup