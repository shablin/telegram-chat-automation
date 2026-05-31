import asyncio
from pathlib import Path
from ollama import AsyncClient as OllamaClient

from config import OLLAMA_URL
from config import OLLAMA_MODEL
from config import OLLAMA_TIMEOUT


def _get_system_prompt():
    SYSTEM_PROMPT = Path(
        "prompts/system.md"
    ).read_text(
        encoding="utf-8"
    )

    return SYSTEM_PROMPT


async def ask_llm(message: str) -> str:
    async with asyncio.timeout(OLLAMA_TIMEOUT):
        async with OllamaClient(host=OLLAMA_URL) as client:
            try:
                system_prompt = _get_system_prompt()
                response = await client.chat(
                    model=OLLAMA_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": message},
                    ]
                )

                return response["message"]["content"]
            except asyncio.CancelledError:
                print("ollama timeout:", OLLAMA_TIMEOUT)
                return "I'm sorry, can't respond now. Try again later"
            except Exception:
                return "Something went wrong. Try again later"