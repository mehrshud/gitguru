import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration from environment variables or config file
config: Dict[str, str] = {
    'GIT_REPO_DIR': '/path/to/repo',
    'DB_HOST': 'localhost',
    'DB_PORT': '5432'
}

def load_config() -> Dict[str, str]:
    """
    Load configuration from environment variables or config file.
    
    Returns:
        Dict[str, str]: Dictionary containing configuration settings.
    """
    try:
        # Load config from file or environment variables
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {str(e)}")
        raise

def get_logger() -> logging.Logger:
    """
    Get the logger instance.
    
    Returns:
        logging.Logger: Logger instance.
    """
    return logger

def handle_error(err: Exception) -> None:
    """
    Handle errors by logging them.
    
    Args:
        err (Exception): Error to be handled.
    """
    logger.error(f"Error occurred: {str(err)}")
