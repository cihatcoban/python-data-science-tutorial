"""
Structured logging module ensuring high observability without silent failures.
"""

import logging
import sys
from typing import Optional


def get_logger(name: str = "datascience_toolbox", level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard logger.

    Args:
        name: Name of the logger.
        level: Logging level (e.g. logging.INFO, logging.DEBUG).

    Returns:
        Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
