"""
Data cleaning and preprocessing module implementing robust transformation standards.
"""

from typing import List, Optional, Union
import pandas as pd
import numpy as np

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


class DataCleaner:
    """
    Handles standard tabular cleaning operations:
    - Missing value imputation
    - Column name normalization
    - Duplicate row removal
    """

    def __init__(
        self,
        fill_numeric_strategy: str = "median",
        fill_categorical_strategy: str = "mode",
        drop_duplicates: bool = True,
    ):
        self.fill_numeric_strategy = fill_numeric_strategy
        self.fill_categorical_strategy = fill_categorical_strategy
        self.drop_duplicates = drop_duplicates

    def normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardizes column names to lowercase with underscores."""
        df = df.copy()
        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^\w_]", "", regex=True)
        )
        return df

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Imputes missing values based on configured strategies."""
        df = df.copy()
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if pd.api.types.is_numeric_dtype(df[col]):
                    val = df[col].median() if self.fill_numeric_strategy == "median" else df[col].mean()
                    df[col] = df[col].fillna(val)
                else:
                    mode_series = df[col].mode()
                    val = mode_series[0] if not mode_series.empty else "Unknown"
                    df[col] = df[col].fillna(val)
        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Executes full cleaning pipeline."""
        logger.info(f"Starting data cleaning on dataframe of shape {df.shape}")
        cleaned = self.normalize_columns(df)
        if self.drop_duplicates:
            cleaned = cleaned.drop_duplicates()
        cleaned = self.handle_missing_values(cleaned)
        logger.info(f"Data cleaning finished. Cleaned shape: {cleaned.shape}")
        return cleaned
