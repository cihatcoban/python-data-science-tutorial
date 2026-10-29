"""
Custom Scikit-Learn compatible transformers for feature engineering.
Includes resilient fallback when scikit-learn is not installed.
"""

from typing import List, Optional
import numpy as np
import pandas as pd

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except ImportError:
    class BaseEstimator:
        pass

    class TransformerMixin:
        def fit_transform(self, X, y=None, **fit_params):
            return self.fit(X, y, **fit_params).transform(X)

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


class OutlierCapper(BaseEstimator, TransformerMixin):
    """
    Caps numerical outliers using Tukey's Interquartile Range (IQR) method.
    Prevents extreme values from skewing linear and distance-based estimators.
    """

    def __init__(self, factor: float = 1.5, columns: Optional[List[str]] = None):
        self.factor = factor
        self.columns = columns
        self.bounds_: dict = {}

    def fit(self, X: pd.DataFrame, y=None):
        """Calculates lower and upper bounds for each numeric feature."""
        df = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)
        cols = self.columns if self.columns is not None else df.select_dtypes(include=[np.number]).columns

        self.bounds_ = {}
        for col in cols:
            q1 = float(df[col].quantile(0.25))
            q3 = float(df[col].quantile(0.75))
            iqr = q3 - q1
            lower = q1 - (self.factor * iqr)
            upper = q3 + (self.factor * iqr)
            self.bounds_[col] = (lower, upper)

        logger.info(f"Fitted OutlierCapper on {len(self.bounds_)} numeric columns with factor={self.factor}")
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Clips values in columns to the learned boundaries."""
        df = X.copy() if isinstance(X, pd.DataFrame) else pd.DataFrame(X).copy()
        for col, (lower, upper) in self.bounds_.items():
            if col in df.columns:
                df[col] = df[col].clip(lower=lower, upper=upper)
        return df
