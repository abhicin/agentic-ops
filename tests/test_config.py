import os
import tempfile
from ops_agents import load_config


def test_load_config_from_file():
    yaml_content = """
    database:
      connection_string: sqlite:///tmp.db
    jira:
      url: https://jira.local
    github:
      token: testtoken
    servicenow:
      url: https://sn.local
    """
    with tempfile.NamedTemporaryFile('w+', delete=False) as f:
        f.write(yaml_content)
        path = f.name
    try:
        cfg = load_config(path)
        assert cfg.database_url == "sqlite:///tmp.db"
        assert cfg.jira_url == "https://jira.local"
        assert cfg.github_token == "testtoken"
        assert cfg.servicenow_url == "https://sn.local"
    finally:
        os.remove(path)

