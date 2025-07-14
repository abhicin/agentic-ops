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

## Configuration file

Agents can optionally read connection details for external systems from a YAML
configuration file. The orchestrator automatically loads ``ops_config.yml`` from
the project root or the path specified by the ``OPS_CONFIG_FILE`` environment
variable. A sample configuration might look like:

```yaml
database:
  connection_string: postgresql://user:pass@localhost/db
jira:
  url: https://jira.example.com
github:
  token: ghp_exampletoken
servicenow:
  url: https://servicenow.example.com
```

Pass the loaded configuration to agents or let the ``Orchestrator`` do so
automatically:

```python
from ops_agents import Orchestrator, load_config

config = load_config()
orch = Orchestrator(config=config)
```

Each agent receives the configuration object and can use the values to connect
to databases, JIRA, GitHub or ServiceNow.

