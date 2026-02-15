import logging
from typing import Dict
import yaml

# Load configuration from YAML file
with open('config.yaml', 'r') as f:
    config: Dict = yaml.safe_load(f)

# Set up logging
logging.basicConfig(level=config['logging_level'])
logger = logging.getLogger(__name__)

def handle_error(exception: Exception) -> None:
    """Handle errors in a professional and secure manner."""
    logger.error(f"Error occurred: {exception}")

def get_config(key: str) -> str:
    """Retrieve configuration value by key."""
    try:
        return config[key]
    except KeyError:
        handle_error(f"Missing configuration key: {key}")
        return None

# Example usage:
if __name__ == "__main__":
    logging_level = get_config('logging_level')
    logger.info(f"Logging level: {logging_level}")
