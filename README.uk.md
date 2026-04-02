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

<h3 align="center">Маркетплейс кредитів на AI-обчислення</h3>

<p align="center">
  Перетворіть $1M фінансування на $1.25-1.5M обчислювальних кредитів.<br>
  OpenAI-сумісний API. Мультипровайдер. Без прив'язки.
</p>

<p align="center">
  <a href="https://github.com/CompuX-ai/docs/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://compux.ai"><img src="https://img.shields.io/badge/website-compux.ai-brightgreen" alt="Website"></a>
  <a href="https://docs.compux.ai"><img src="https://img.shields.io/badge/API_Docs-docs.compux.ai-blue" alt="API Docs"></a>
  <a href="https://learn-compux.kossanstin.workers.dev"><img src="https://img.shields.io/badge/Learn-Knowledge_Base-orange" alt="Learn"></a>
  <a href="https://twitter.com/compux_ai"><img src="https://img.shields.io/twitter/follow/compux_ai" alt="Twitter"></a>
</p>

---

## Що таке CompuX?

CompuX — це **тристоронній маркетплейс**, що з'єднує AI-стартапи, провайдерів обчислень та фінансових партнерів. Ми перетворюємо фінансування на обчислювальні кредити з множником 25-50% — $1M стає $1.25-1.5M корисних обчислень.

**Заміна OpenAI без змін коду.** Змініть один рядок:

```python
# До (OpenAI)
from openai import OpenAI
client = OpenAI(api_key="sk-...")

# Після (CompuX) — той самий SDK, той самий API, на 25-50% дешевше
from openai import OpenAI
client = OpenAI(
    api_key="your-compux-key",
    base_url="https://api.compux.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Привіт від CompuX!"}]
)
```

## Чому CompuX?

- **Економія 25-50%** завдяки фінансуванню обчислювальних кредитів (не знижки — реальний фінансовий множник)
- **OpenAI-сумісний API** — пряма заміна, нуль змін у коді
- **Мультипровайдер** — OpenAI, Anthropic, Google, Mistral, open-source моделі
- **Блоковані кредити** — забезпечені обчислення, які кредитори можуть заморожувати/розморожувати
- **Без прив'язки** — змінюйте провайдерів будь-коли, зберігайте кредити

## Документація

### База знань (Learn)

Глибокі статті про економіку AI-обчислень, фінансування та інфраструктуру.

| Розділ | Сторінок | Що ви дізнаєтесь |
|--------|----------|-------------------|
| [Концепції](concepts/) | 34 | Обчислювальні кредити, токен-оператори, GPU-економіка, LLM-маршрутизація |
| [Порівняння](compare/) | 9 | CompuX vs OpenRouter, Together AI, Lambda Labs, венчурний борг |
| [Кейси](use-cases/) | 7 | Стартапи, кредитори, GPU-провайдери, dev tools |
| [FAQ](faq/) | 10 | 490 питань і відповідей про ціни, інтеграцію, забезпечення |

### Довідник API

Повна документація API доступна на **[docs.compux.ai](https://docs.compux.ai)**.

- [Chat Completions](https://docs.compux.ai/docs/api-reference/chat-completions) — OpenAI-сумісний endpoint
- [Автентифікація](https://docs.compux.ai/docs/authentication/api-keys) — API-ключі та JWT
- [Моделі](https://docs.compux.ai/docs/api-reference/models) — Доступні моделі та провайдери
- [Швидкий старт](https://docs.compux.ai/docs/getting-started/quickstart) — Запуск за 5 хвилин

## Швидкий старт

### 1. Отримайте API-ключ

Зареєструйтесь на [app.compux.ai](https://app.compux.ai/register) та створіть API-ключ.

### 2. Зробіть перший запит

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Привіт!"}]
  }'
```

### 3. Використовуйте з будь-яким OpenAI-сумісним SDK

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

## Як це працює

```
AI-стартап                    CompuX                      Провайдер обчислень
    |                           |                               |
    |-- Потрібні обчислення ---->|                               |
    |                           |-- Фінансування ($1M) -------->|
    |                           |<-- Кредити ($1.25-1.5M) ------|
    |<-- Блоковані кредити -----|                               |
    |                           |                               |
    |-- API-запит (OpenAI) ---->|-- Маршрут до провайдера ----->|
    |<-- Відповідь -------------|<-- Відповідь -----------------|
```

**Рівень 5: Токен-оператор** — CompuX працює на 5-му рівні ланцюга створення цінності AI, між інфраструктурою (GPU) та додатками (AI-продукти). Ми оптимізуємо потік обчислювальних кредитів як фінансовий оператор.

## Ключові концепції

| Концепція | Опис |
|-----------|------|
| **Обчислювальні кредити** | Стандартизовані одиниці обчислень між провайдерами |
| **Кредитна трансфузія** | Конвертація фінансування у збільшені обчислювальні кредити |
| **Блоковані кредити** | Кредити, які можна заморожувати/розморожувати як забезпечення |
| **Токен-оператор** | Сутність рівня 5, що управляє потоком обчислювальних кредитів |
| **Мультипровайдерна маршрутизація** | Автоматичний вибір оптимального провайдера для кожного запиту |

Читайте більше у розділі [Концепції](concepts/).

## Спільнота та підтримка

- [Вебсайт](https://compux.ai) — Дізнайтесь про CompuX
- [База знань](https://learn-compux.kossanstin.workers.dev) — Глибокі статті та гайди
- [API Docs](https://docs.compux.ai) — Довідник API
- [Twitter](https://twitter.com/compux_ai) — Оновлення та анонси
- [LinkedIn](https://www.linkedin.com/company/compux) — Новини компанії
- [GitHub](https://github.com/CompuX-ai) — Open source проекти
- [Зв'язатись](https://compux.ai/get-in-touch) — Напишіть нам

## Внесок

Ми вітаємо внески! Дивіться [CONTRIBUTING.md](CONTRIBUTING.md) для інструкцій.

## Ліцензія

Цей проект ліцензовано під MIT License — дивіться [LICENSE](LICENSE) для деталей.