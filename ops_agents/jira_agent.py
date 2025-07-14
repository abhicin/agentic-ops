from .base import Agent
from .llm import LLM


class JiraAgent(Agent):
    """Agent responsible for JIRA ticket management."""

    def __init__(self, llm: LLM | None = None):
        super().__init__("jira")
        self.llm = llm or LLM()

    def run(self, prompt: str) -> str:
        query = f"Work with JIRA: {prompt}"
        return self.llm.complete(query)
