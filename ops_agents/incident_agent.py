from .base import Agent
from .llm import LLM


class IncidentAgent(Agent):
    """Agent responsible for incident management."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("incident")
        self.llm = llm or LLM()

    def run(self, prompt: str) -> str:
        query = f"Investigate incident: {prompt}"
        return self.llm.complete(query)
