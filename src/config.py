import logging
import os
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    def __init__(self) -> None:
        """
        Initialize configuration with default values.
        """
        self.debug: bool = False
        self.graphql_schema: str = "schema.graphql"
        self.git_repo_path: str = "/path/to/repo"
        self.db_uri: str = "sqlite:///gitguru.db"

    def load_from_env(self) -> None:
        """
        Load configuration from environment variables.
        """
        self.debug = os.environ.get("DEBUG", "false").lower() == "true"
        self.graphql_schema = os.environ.get("GRAPHQL_SCHEMA", self.graphql_schema)
        self.git_repo_path = os.environ.get("GIT_REPO_PATH", self.git_repo_path)
        self.db_uri = os.environ.get("DB_URI", self.db_uri)

    def to_dict(self) -> Dict[str, str]:
        """
        Convert configuration to dictionary.
        """
        return {
            "debug": str(self.debug),
            "graphql_schema": self.graphql_schema,
            "git_repo_path": self.git_repo_path,
            "db_uri": self.db_uri,
        }

def get_config() -> Config:
    """
    Get the application configuration.
    """
    config = Config()
    config.load_from_env()
    return config

config = get_config()
logger.info("Loaded configuration: %s", config.to_dict())
