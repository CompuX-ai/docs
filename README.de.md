<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">中文</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.uk.md">Українська</a>
</p>

<p align="center">
  <img src="https://compux.ai/logo.svg" alt="CompuX" width="200">
</p>

<h3 align="center">AI-Rechenkredit-Marktplatz</h3>

<p align="center">
  Wandeln Sie 1 Mio. $ Finanzierung in 1,25-1,5 Mio. $ Rechenkredite um.<br>
  OpenAI-kompatible API. Multi-Provider. Kein Lock-in.
</p>

<p align="center">
  <a href="https://github.com/CompuX-ai/docs/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://compux.ai"><img src="https://img.shields.io/badge/website-compux.ai-brightgreen" alt="Website"></a>
  <a href="https://docs.compux.ai"><img src="https://img.shields.io/badge/API_Docs-docs.compux.ai-blue" alt="API Docs"></a>
  <a href="https://learn-compux.kossanstin.workers.dev"><img src="https://img.shields.io/badge/Learn-Knowledge_Base-orange" alt="Learn"></a>
  <a href="https://twitter.com/compux_ai"><img src="https://img.shields.io/twitter/follow/compux_ai" alt="Twitter"></a>
</p>

---

## Was ist CompuX?

CompuX ist ein **dreiseitiger Marktplatz**, der AI-Startups, Rechenanbieter und Kapitalpartner verbindet. Wir wandeln Finanzierung in Rechenkredite mit einem 25-50% Multiplikator um — aus 1 Mio. $ werden 1,25-1,5 Mio. $ nutzbare Rechenleistung.

**Direkter OpenAI-Ersatz.** Nur eine Zeile Code andern:

```python
# Vorher (OpenAI)
from openai import OpenAI
client = OpenAI(api_key="sk-...")

# Nachher (CompuX) — gleiches SDK, gleiche API, 25-50% gunstiger
from openai import OpenAI
client = OpenAI(
    api_key="your-compux-key",
    base_url="https://api.compux.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hallo von CompuX!"}]
)
```

## Warum CompuX?

- **25-50% Kosteneinsparung** durch Rechenkredit-Finanzierung (keine Rabatte — echter finanzieller Multiplikator)
- **OpenAI-kompatible API** — Drop-in-Ersatz, null Code-Anderungen
- **Multi-Provider** — OpenAI, Anthropic, Google, Mistral, Open-Source-Modelle
- **Sperrbare Kredite** — besicherbare Rechenleistung, die Kreditgeber einfrieren/freigeben konnen
- **Kein Lock-in** — jederzeit Anbieter wechseln, Kredite behalten

## Dokumentation

### Wissensdatenbank (Learn)

Ausfuhrliche Artikel uber AI-Rechenokonomie, Finanzierung und Infrastruktur.

| Bereich | Seiten | Was Sie lernen |
|---------|--------|----------------|
| [Konzepte](concepts/) | 34 | Rechenkredite, Token-Operatoren, GPU-Okonomie, LLM-Routing |
| [Vergleiche](compare/) | 9 | CompuX vs OpenRouter, Together AI, Lambda Labs, Venture Debt |
| [Anwendungsfalle](use-cases/) | 7 | Startups, Kreditgeber, GPU-Anbieter, Dev Tools |
| [FAQ](faq/) | 10 | 490 Fragen und Antworten zu Preisen, Integration, Sicherheiten |

### API-Referenz

Vollstandige API-Dokumentation unter **[docs.compux.ai](https://docs.compux.ai)**.

- [Chat Completions](https://docs.compux.ai/docs/api-reference/chat-completions) — OpenAI-kompatibler Endpunkt
- [Authentifizierung](https://docs.compux.ai/docs/authentication/api-keys) — API-Schlussel und JWT-Auth
- [Modelle](https://docs.compux.ai/docs/api-reference/models) — Verfugbare Modelle und Anbieter
- [Schnellstart](https://docs.compux.ai/docs/getting-started/quickstart) — In 5 Minuten starten

## Schnellstart

### 1. API-Schlussel erhalten

Registrieren Sie sich bei [app.compux.ai](https://app.compux.ai/register) und erstellen Sie einen API-Schlussel.

### 2. Erste Anfrage senden

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hallo!"}]
  }'
```

### 3. Mit jedem OpenAI-kompatiblen SDK verwenden

```python
# Python
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.compux.ai/v1")
```

```typescript
// TypeScript
import OpenAI from 'openai';
const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://api.compux.ai/v1' });
```

## So funktioniert es

```
AI-Startup                    CompuX                      Rechenanbieter
    |                           |                               |
    |-- Braucht Rechenleistung->|                               |
    |                           |-- Finanzierung ($1M) -------->|
    |                           |<-- Kredite ($1.25-1.5M) ------|
    |<-- Sperrbare Kredite -----|                               |
    |                           |                               |
    |-- API-Anfrage (OpenAI) -->|-- Route zum besten Anbieter ->|
    |<-- Antwort ---------------|<-- Antwort -------------------|
```

**Schicht 5: Token-Operator** — CompuX operiert auf Schicht 5 der AI-Wertschopfungskette, zwischen Infrastruktur (GPUs) und Anwendungen (AI-Produkte). Wir optimieren den Fluss von Rechenkrediten wie ein Finanzoperator.

## Schlusselkonzepte

| Konzept | Beschreibung |
|---------|-------------|
| **Rechenkredite** | Standardisierte Recheneinheiten uber Anbieter hinweg |
| **Kredit-Transfusion** | Umwandlung von Finanzierung in verstarkte Rechenkredite |
| **Sperrbare Kredite** | Kredite, die als Sicherheit eingefroren/freigegeben werden konnen |
| **Token-Operator** | Schicht-5-Entitat zur Verwaltung des Rechenkreditflusses |
| **Multi-Provider-Routing** | Automatische Auswahl des optimalen Anbieters pro Anfrage |

Mehr erfahren im Bereich [Konzepte](concepts/).

## Community und Support

- [Website](https://compux.ai) — Uber CompuX
- [Wissensdatenbank](https://learn-compux.kossanstin.workers.dev) — Ausfuhrliche Artikel und Anleitungen
- [API Docs](https://docs.compux.ai) — API-Referenz
- [Twitter](https://twitter.com/compux_ai) — Updates und Ankundigungen
- [LinkedIn](https://www.linkedin.com/company/compux) — Unternehmensnachrichten
- [GitHub](https://github.com/CompuX-ai) — Open-Source-Projekte
- [Kontakt](https://compux.ai/get-in-touch) — Sprechen Sie mit uns

## Beitragen

Beitrage sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) fur Richtlinien.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert — siehe [LICENSE](LICENSE) fur Details.