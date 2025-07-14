from .base import Agent
from .llm import LLM, OpenAILLM
from .config import Config


class IncidentAgent(Agent):
    """Agent responsible for incident management."""

    def __init__(self, llm: LLM | None = None, config: Config | None = None):
        super().__init__("incident")
        self.llm = llm or OpenAILLM()
        self.config = config

    def run(self, prompt: str) -> str:
        query = f"Investigate incident: {prompt}"
        return self.llm.complete(query)
