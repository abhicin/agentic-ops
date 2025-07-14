from .base import Agent
from .llm import LLM, OpenAILLM
from .config import Config


class JiraAgent(Agent):
    """Agent responsible for JIRA ticket management."""

    def __init__(self, llm: LLM | None = None, config: Config | None = None):
        super().__init__("jira")
        self.llm = llm or OpenAILLM()
        self.config = config

    def run(self, prompt: str) -> str:
        query = f"Work with JIRA: {prompt}"
        return self.llm.complete(query)
