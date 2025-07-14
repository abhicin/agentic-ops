# agentic-ops

This repository provides a simple multi-agent framework for operational intelligence.

## Overview

The system defines several agents that use large language models (LLMs) to
understand requests and perform tasks. An `Orchestrator` routes a user prompt to
the appropriate agent based on keywords.

Agents included:

- **LogAgent** – analyzes log data
- **CodeAgent** – assists with code questions
- **DatabaseAgent** – handles database related operations
- **IncidentAgent** – responds to incidents and outages
- **JiraAgent** – works with JIRA tickets

Each agent uses a lightweight LLM wrapper (by default the OpenAI API) to
generate responses. To try it out, create an orchestrator and dispatch a
prompt:

```python
from ops_agents import Orchestrator

orch = Orchestrator()
result = orch.dispatch("investigate incident 123")
print(result.agent, result.response)
```

Set the `OPENAI_API_KEY` environment variable to enable LLM calls.
