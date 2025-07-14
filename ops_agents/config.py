from __future__ import annotations

"""Configuration loader for external service connections."""

from dataclasses import dataclass
import os
import yaml


@dataclass
class Config:
    """Configuration values for external service connections."""

    database_url: str | None = None
    jira_url: str | None = None
    github_token: str | None = None
    servicenow_url: str | None = None


def load_config(path: str | None = None) -> Config:
    """Load configuration from a YAML file.

    The file path can be provided explicitly or via the ``OPS_CONFIG_FILE``
    environment variable. If no file is found, an empty ``Config`` object is
    returned.
    """
    path = path or os.getenv("OPS_CONFIG_FILE", "ops_config.yml")
    if not os.path.exists(path):
        return Config()
    with open(path, "r") as f:
        data = yaml.safe_load(f) or {}
    return Config(
        database_url=data.get("database", {}).get("connection_string"),
        jira_url=data.get("jira", {}).get("url"),
        github_token=data.get("github", {}).get("token"),
        servicenow_url=data.get("servicenow", {}).get("url"),
    )
