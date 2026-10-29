"""
Model evaluation module producing comprehensive metrics for regression and classification.
Includes pure-Python / numpy fallback when scikit-learn is not yet installed in runtime.
"""

from typing import Dict, Optional
import numpy as np

try:
    from sklearn.metrics import (
        mean_squared_error,
        mean_absolute_error,
        r2_score,
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        roc_auc_score,
    )
    _SKLEARN_AVAILABLE = True
except ImportError:
    _SKLEARN_AVAILABLE = False

from datascience_toolbox.utils.logger import get_logger

logger = get_logger(__name__)


def evaluate_regression(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Computes standard regression evaluation metrics (RMSE, MAE, R2)."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if _SKLEARN_AVAILABLE:
        mse = mean_squared_error(y_true, y_pred)
        rmse = float(np.sqrt(mse))
        mae = float(mean_absolute_error(y_true, y_pred))
        r2 = float(r2_score(y_true, y_pred))
    else:
        mse = float(np.mean((y_true - y_pred) ** 2))
        rmse = float(np.sqrt(mse))
        mae = float(np.mean(np.abs(y_true - y_pred)))
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r2 = float(1 - (ss_res / ss_tot)) if ss_tot != 0 else 0.0

    metrics = {
        "rmse": round(rmse, 4),
        "mae": round(mae, 4),
        "r2_score": round(r2, 4),
    }
    logger.info(f"Regression evaluation: {metrics}")
    return metrics


def evaluate_classification(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray] = None
) -> Dict[str, float]:
    """Computes standard classification evaluation metrics."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if _SKLEARN_AVAILABLE:
        acc = float(accuracy_score(y_true, y_pred))
        prec = float(precision_score(y_true, y_pred, average="weighted", zero_division=0))
        rec = float(recall_score(y_true, y_pred, average="weighted", zero_division=0))
        f1 = float(f1_score(y_true, y_pred, average="weighted", zero_division=0))
    else:
        acc = float(np.mean(y_true == y_pred))
        prec = acc  # Simple fallback
        rec = acc
        f1 = acc

    metrics = {
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4),
    }

    if y_prob is not None and _SKLEARN_AVAILABLE:
        try:
            if len(np.unique(y_true)) == 2:
                auc = float(roc_auc_score(y_true, y_prob[:, 1] if y_prob.ndim == 2 else y_prob))
            else:
                auc = float(roc_auc_score(y_true, y_prob, multi_class="ovr"))
            metrics["roc_auc"] = round(auc, 4)
        except Exception as e:
            logger.warning(f"Could not compute ROC-AUC: {e}")

    logger.info(f"Classification evaluation: {metrics}")
    return metrics
