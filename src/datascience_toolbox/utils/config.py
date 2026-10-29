"""
Configuration manager loading and validating YAML settings.
"""

from pathlib import Path
from typing import Any, Dict
import yaml

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


def load_config(config_path: str = "configs/config.yaml") -> Dict[str, Any]:
    """
    Loads YAML configuration safely with explicit error propagation.

    Args:
        config_path: Relative or absolute path to the YAML file.

    Returns:
        Dictionary containing project configurations.

    Raises:
        FileNotFoundError: If configuration file does not exist.
        yaml.YAMLError: If YAML syntax is invalid.
    """
    path = Path(config_path)
    if not path.is_file():
        logger.error(f"Config file not found at: {path.resolve()}")
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        logger.info(f"Loaded configuration from {config_path}")
        return config or {}
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML config: {e}")
        raise
