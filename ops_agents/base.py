class Agent:
    """Base class for all agents."""
    def __init__(self, name: str):
        self.name = name

    def run(self, prompt: str) -> str:
        raise NotImplementedError("Agents must implement the run method")
