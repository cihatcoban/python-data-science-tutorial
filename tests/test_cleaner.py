"""Unit tests for data cleaner module."""

import unittest
import pandas as pd
import numpy as np
from datascience_toolbox.data.cleaner import DataCleaner


class TestDataCleaner(unittest.TestCase):
    def test_normalize_columns(self):
        df = pd.DataFrame({" First Name ": [1], "Exam #1": [2], "City/Region": [3]})
        cleaner = DataCleaner()
        cleaned = cleaner.normalize_columns(df)
        self.assertEqual(list(cleaned.columns), ["first_name", "exam_1", "cityregion"])

    def test_handle_missing_values(self):
        df = pd.DataFrame({
            "num": [10.0, 20.0, np.nan, 40.0],
            "cat": ["A", "B", np.nan, "A"]
        })
        cleaner = DataCleaner(fill_numeric_strategy="median")
        cleaned = cleaner.handle_missing_values(df)

        self.assertEqual(cleaned["num"].isnull().sum(), 0)
        self.assertEqual(cleaned["num"].iloc[2], 20.0)
        self.assertEqual(cleaned["cat"].isnull().sum(), 0)
        self.assertEqual(cleaned["cat"].iloc[2], "A")


if __name__ == "__main__":
    unittest.main()
