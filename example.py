"""Example usage of the Orchestrator."""
from ops_agents import Orchestrator


def main():
    orch = Orchestrator()
    result = orch.dispatch("show me the database logs for outage")
    print(f"Agent: {result.agent}\nResponse: {result.response}")


if __name__ == "__main__":
    main()
