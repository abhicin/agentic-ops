from .base import Agent
from .llm import LLM, OpenAILLM


class LogAgent(Agent):
    """Agent responsible for log analysis."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("log")
        self.llm = llm or OpenAILLM()

    def run(self, prompt: str) -> str:
        # In reality this would parse and analyze logs
        query = f"Analyze logs for: {prompt}"
        return self.llm.complete(query)
