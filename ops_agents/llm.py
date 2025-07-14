"""Simple LLM wrapper using OpenAI's API if available."""

from __future__ import annotations

import os
from typing import Optional

try:
    import openai
except ImportError:  # pragma: no cover - if openai isn't installed
    openai = None


class LLM:
    """LLM interface for generating responses."""

    def __init__(self, model: str = "gpt-3.5-turbo", api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if openai and self.api_key:
            openai.api_key = self.api_key

    def complete(self, prompt: str) -> str:
        if not (openai and self.api_key):
            return f"[LLM unavailable] {prompt}"
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
