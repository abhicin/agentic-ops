import pytest
from ops_agents import Orchestrator, Config

class FakeLLM:
    def __init__(self):
        self.prompts = []
    def complete(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return f"mock-{prompt}"

def make_orchestrator():
    orch = Orchestrator()
    # replace llm instances with fakes
    for agent in [
        orch.log_agent,
        orch.code_agent,
        orch.db_agent,
        orch.incident_agent,
        orch.jira_agent,
    ]:
        agent.llm = FakeLLM()
    return orch

@pytest.mark.parametrize(
    "prompt,agent,query",
    [
        ("show logs for 500 error", "log", "Analyze logs for: show logs for 500 error"),
        ("update code in repo", "code", "Assist with code for: update code in repo"),
        ("run sql query", "database", "Handle database task: run sql query"),
        ("incident 42 ongoing", "incident", "Investigate incident: incident 42 ongoing"),
        ("create jira ticket", "jira", "Work with JIRA: create jira ticket"),
        ("hello world", "code", "Assist with code for: hello world"),
        (
            "why is task ID or request ID for example - TID1234 failing ? check if issue was caused by recent code changes",
            "code",
            "Assist with code for: why is task ID or request ID for example - TID1234 failing ? check if issue was caused by recent code changes",
        ),
        (
            "give me processing time and latency of task ID for example - TID4567",
            "code",
            "Assist with code for: give me processing time and latency of task ID for example - TID4567",
        ),
    ],
)
def test_dispatch_routing(prompt, agent, query):
    orch = make_orchestrator()
    result = orch.dispatch(prompt)
    assert result.agent == agent
    assert result.response == f"mock-{query}"


def test_agent_query_used():
    orch = make_orchestrator()
    result = orch.dispatch("check logs now")
    assert result.agent == "log"
    assert orch.log_agent.llm.prompts[-1] == "Analyze logs for: check logs now"
    assert result.response == "mock-Analyze logs for: check logs now"


def test_config_passed_to_agents():
    cfg = Config(database_url="sqlite:///db.sqlite")
    orch = Orchestrator(config=cfg)
    assert orch.log_agent.config is cfg
    assert orch.code_agent.config is cfg
    assert orch.db_agent.config is cfg
    assert orch.incident_agent.config is cfg
    assert orch.jira_agent.config is cfg
