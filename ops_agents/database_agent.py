from .base import Agent
from .llm import LLM


class DatabaseAgent(Agent):
    """Agent responsible for database queries or analysis."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("database")
        self.llm = llm or LLM()

    def run(self, prompt: str) -> str:
        query = f"Handle database task: {prompt}"
        return self.llm.complete(query)
