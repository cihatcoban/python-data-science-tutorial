"""
Data loader module with path validation, defensive file checking, and logging.
"""

from pathlib import Path
from typing import Optional, Union
import pandas as pd

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


def load_dataset(
    file_path: Union[str, Path],
    file_format: Optional[str] = None,
    **kwargs
) -> pd.DataFrame:
    """
    Loads a tabular dataset from disk (CSV or Parquet) with validation.

    Args:
        file_path: Path to dataset file.
        file_format: Explicit format ('csv', 'parquet'). If None, inferred from extension.
        **kwargs: Additional parameters passed to pd.read_csv or pd.read_parquet.

    Returns:
        Loaded pandas DataFrame.

    Raises:
        FileNotFoundError: If the target file does not exist.
        ValueError: If file format is unsupported.
    """
    path = Path(file_path)
    if not path.is_file():
        logger.error(f"Target data file does not exist: {path.resolve()}")
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    ext = (file_format or path.suffix.lstrip(".")).lower()

    if ext == "csv":
        df = pd.read_csv(path, **kwargs)
    elif ext in ("parquet", "pq"):
        df = pd.read_parquet(path, **kwargs)
    else:
        raise ValueError(f"Unsupported data format '{ext}'. Supported formats: ['csv', 'parquet']")

    logger.info(f"Successfully loaded dataset '{path.name}' with shape {df.shape}")
    return df
