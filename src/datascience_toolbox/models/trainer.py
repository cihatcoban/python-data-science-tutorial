"""
Model training orchestrator supporting cross-validation and pipeline execution.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


def train_baseline_regressor(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
    n_estimators: int = 100,
) -> Tuple[Any, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Trains a baseline Random Forest Regressor ensuring proper train-test split without data leakage.

    Returns:
        Tuple of (trained_model, X_train, X_test, y_train, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    logger.info(f"Train set: {X_train.shape}, Test set: {X_test.shape}")

    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    logger.info("RandomForestRegressor training completed successfully.")
    return model, X_train, X_test, y_train, y_test
