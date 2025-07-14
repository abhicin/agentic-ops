from .base import Agent
from .llm import LLM


class CodeAgent(Agent):
    """Agent responsible for code analysis or generation."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("code")
        self.llm = llm or LLM()

    def run(self, prompt: str) -> str:
        query = f"Assist with code for: {prompt}"
        return self.llm.complete(query)
