from __future__ import annotations

from dataclasses import dataclass

from .base import Agent
from .llm import LLM, OpenAILLM
from .config import Config, load_config
from .log_agent import LogAgent
from .code_agent import CodeAgent
from .database_agent import DatabaseAgent
from .incident_agent import IncidentAgent
from .jira_agent import JiraAgent


@dataclass
class OrchestrationResult:
    agent: str
    response: str


class Orchestrator:
    """Route a prompt to the appropriate agent based on simple heuristics."""

    def __init__(self, llm: LLM | None = None, config: Config | None = None):
        llm = llm or OpenAILLM()
        self.config = config or load_config()
        self.log_agent = LogAgent(llm=llm, config=self.config)
        self.code_agent = CodeAgent(llm=llm, config=self.config)
        self.db_agent = DatabaseAgent(llm=llm, config=self.config)
        self.incident_agent = IncidentAgent(llm=llm, config=self.config)
        self.jira_agent = JiraAgent(llm=llm, config=self.config)

    def dispatch(self, prompt: str) -> OrchestrationResult:
        lowered = prompt.lower()
        agent: Agent
        if any(key in lowered for key in ["log", "logs"]):
            agent = self.log_agent
        elif any(key in lowered for key in ["code", "repo", "git"]):
            agent = self.code_agent
        elif any(key in lowered for key in ["db", "database", "sql"]):
            agent = self.db_agent
        elif any(key in lowered for key in ["incident", "alert", "outage"]):
            agent = self.incident_agent
        elif any(key in lowered for key in ["jira", "ticket"]):
            agent = self.jira_agent
        else:
            agent = self.code_agent  # default

        response = agent.run(prompt)
        return OrchestrationResult(agent=agent.name, response=response)
