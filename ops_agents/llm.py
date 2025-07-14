"""LLM backends and interfaces used by the agents."""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Optional

try:  # pragma: no cover - optional dependency
    import openai
except ImportError:  # pragma: no cover - if openai isn't installed
    openai = None


class LLM(ABC):
    """Abstract interface for generating responses from a language model."""

    @abstractmethod
    def complete(self, prompt: str) -> str:
        """Return a completion for ``prompt``."""


class OpenAILLM(LLM):
    """Default backend using OpenAI's chat completion API."""

    def __init__(self, model: str = "gpt-3.5-turbo", api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if openai and self.api_key:
            openai.api_key = self.api_key

    def complete(self, prompt: str) -> str:
        if not (openai and self.api_key):
            return f"[OpenAI LLM unavailable] {prompt}"
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()


# ----- Optional backends -------------------------------------------------

try:  # pragma: no cover - optional dependency
    import langgraph
except ImportError:  # pragma: no cover - optional
    langgraph = None


class LangGraphLLM(LLM):
    """LLM wrapper using LangGraph if available."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model

    def complete(self, prompt: str) -> str:
        if not langgraph:
            return f"[LangGraphLLM unavailable] {prompt}"
        # Placeholder implementation. Real usage would call LangGraph APIs.
        return f"[LangGraph {self.model}] {prompt}"


try:  # pragma: no cover - optional dependency
    import crewai
except ImportError:  # pragma: no cover - optional
    crewai = None


class CrewAILLM(LLM):
    """LLM wrapper using CrewAI if available."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model

    def complete(self, prompt: str) -> str:
        if not crewai:
            return f"[CrewAILLM unavailable] {prompt}"
        return f"[CrewAI {self.model}] {prompt}"


try:  # pragma: no cover - optional dependency
    import semantic_kernel as sk
except ImportError:  # pragma: no cover - optional
    sk = None


class SemanticKernelLLM(LLM):
    """LLM wrapper using Semantic Kernel if available."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model

    def complete(self, prompt: str) -> str:
        if not sk:
            return f"[SemanticKernelLLM unavailable] {prompt}"
        return f"[SemanticKernel {self.model}] {prompt}"


class AzureOpenAILLM(OpenAILLM):
    """OpenAI-compatible backend configured for Azure OpenAI service."""

    def __init__(self, deployment: str, api_base: str, api_version: str = "2023-05-15", api_key: Optional[str] = None):
        super().__init__(model=deployment, api_key=api_key)
        self.api_base = api_base
        self.api_version = api_version
        if openai and self.api_key:
            openai.api_type = "azure"
            openai.api_base = self.api_base
            openai.api_version = self.api_version
