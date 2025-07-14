from .base import Agent
from .llm import LLM, OpenAILLM
from .config import Config


class DatabaseAgent(Agent):
    """Agent responsible for database queries or analysis."""

    def __init__(self, llm: LLM | None = None, config: Config | None = None):
        super().__init__("database")
        self.llm = llm or OpenAILLM()
        self.config = config

    def run(self, prompt: str) -> str:
        query = f"Handle database task: {prompt}"
        return self.llm.complete(query)
