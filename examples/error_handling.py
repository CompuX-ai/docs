"""CompuX Error Handling — Production-ready retry logic with exponential backoff."""

import os
import time
from openai import OpenAI, RateLimitError, APIStatusError, AuthenticationError

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)


def chat(messages: list, model: str = "gpt-4o", max_retries: int = 5) -> str:
    """Send a chat request with automatic retry on transient errors."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            return response.choices[0].message.content

        except AuthenticationError:
            raise  # Don't retry auth errors — fix your API key

        except RateLimitError as e:
            retry_after = int(e.response.headers.get("Retry-After", 2**attempt))
            print(f"Rate limited. Retrying in {retry_after}s (attempt {attempt + 1})")
            time.sleep(retry_after)

        except APIStatusError as e:
            if e.status_code >= 500:
                wait = min(2**attempt, 30)
                print(f"Server error {e.status_code}. Retrying in {wait}s (attempt {attempt + 1})")
                time.sleep(wait)
            else:
                raise  # Don't retry other 4xx errors

    raise RuntimeError(f"Failed after {max_retries} retries")


if __name__ == "__main__":
    result = chat([{"role": "user", "content": "Hello from CompuX!"}])
    print(result)