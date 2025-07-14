from __future__ import annotations

from dataclasses import dataclass

from .base import Agent
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

    def __init__(self):
        self.log_agent = LogAgent()
        self.code_agent = CodeAgent()
        self.db_agent = DatabaseAgent()
        self.incident_agent = IncidentAgent()
        self.jira_agent = JiraAgent()

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
