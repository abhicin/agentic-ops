from .base import Agent
from .llm import LLM, OpenAILLM
from .config import Config


class CodeAgent(Agent):
    """Agent responsible for code analysis or generation."""

    def __init__(self, llm: LLM | None = None, config: Config | None = None):
        super().__init__("code")
        self.llm = llm or OpenAILLM()
        self.config = config

    def run(self, prompt: str) -> str:
        query = f"Assist with code for: {prompt}"
        return self.llm.complete(query)
