from .base import Agent
from .llm import LLM, OpenAILLM


class IncidentAgent(Agent):
    """Agent responsible for incident management."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("incident")
        self.llm = llm or OpenAILLM()

    def run(self, prompt: str) -> str:
        query = f"Investigate incident: {prompt}"
        return self.llm.complete(query)
