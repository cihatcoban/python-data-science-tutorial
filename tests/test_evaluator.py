"""Unit tests for model evaluation metrics."""

import unittest
import numpy as np
from datascience_toolbox.models.evaluator import evaluate_regression, evaluate_classification


class TestEvaluator(unittest.TestCase):
    def test_evaluate_regression(self):
        y_true = np.array([10.0, 20.0, 30.0])
        y_pred = np.array([10.0, 20.0, 30.0])

        metrics = evaluate_regression(y_true, y_pred)
        self.assertEqual(metrics["rmse"], 0.0)
        self.assertEqual(metrics["mae"], 0.0)
        self.assertEqual(metrics["r2_score"], 1.0)

    def test_evaluate_classification(self):
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 1, 0, 1])

        metrics = evaluate_classification(y_true, y_pred)
        self.assertEqual(metrics["accuracy"], 1.0)
        self.assertEqual(metrics["f1_score"], 1.0)


if __name__ == "__main__":
    unittest.main()
