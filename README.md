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


## License

This project is licensed under the [MIT License](LICENSE).

## Configuring LLM backends

Agents accept any implementation of the ``LLM`` interface. The default
``OpenAILLM`` backend uses the OpenAI API but the library also provides several
optional alternatives such as ``LangGraphLLM``, ``CrewAILLM``,
``SemanticKernelLLM`` and ``AzureOpenAILLM``. Pass a backend instance when
constructing the orchestrator or agents:

```python
from ops_agents import Orchestrator, AzureOpenAILLM

llm = AzureOpenAILLM(
    deployment="gpt-35",
    api_base="https://<your-endpoint>.openai.azure.com",
)
orch = Orchestrator(llm=llm)
result = orch.dispatch("check logs")
print(result.response)
```

Set any required API keys (e.g. ``OPENAI_API_KEY``) or service URLs in your
environment variables to activate the chosen backend.

