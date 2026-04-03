# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in CompuX, please report it responsibly.

**Email:** [security@compux.ai](mailto:security@compux.ai)

### What to include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response timeline

| Step | Timeline |
|------|----------|
| Acknowledgment | Within 48 hours |
| Initial assessment | Within 5 business days |
| Fix deployed | Depends on severity (P1: 24hrs, P2: 1 week, P3/P4: next release) |
| Public disclosure | After fix is deployed, coordinated with reporter |

## Supported Versions

| Version | Supported |
|---------|-----------|
| v1.1.x (latest) | Yes |
| v1.0.x | Security fixes only |
| < v1.0 | No |

## Security Practices

CompuX follows industry security standards:

- **Encryption:** TLS 1.3 for all API traffic, AES-256 for data at rest
- **Authentication:** API key-based with per-key scoping
- **Authorization:** Role-based access control (RBAC) for teams
- **Compliance:** SOC 2 Type II (in progress), GDPR-ready, PCI DSS via compliant payment processors
- **Data handling:** API prompts/outputs not stored beyond request lifecycle, never used for training
- **Infrastructure:** DDoS mitigation, real-time anomaly detection, automatic provider failover

For full details, see the [Security & Compliance wiki page](https://github.com/CompuX-ai/compute-credit-financing/wiki/Security-and-Compliance).

## Scope

This policy covers:
- The CompuX API (`api.compux.ai`)
- The CompuX dashboard
- This GitHub repository and its wiki
- The CompuX SDK

Out of scope:
- Third-party GPU provider infrastructure
- Third-party model providers (OpenAI, Anthropic, etc.)

## Recognition

We appreciate security researchers who help keep CompuX safe. With your permission, we'll acknowledge your contribution in our security advisories.