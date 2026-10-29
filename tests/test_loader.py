"""Unit tests for data loader module."""

import unittest
import tempfile
from pathlib import Path
import pandas as pd
from datascience_toolbox.data.loader import load_dataset


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_csv_success(self):
        csv_file = self.tmp_path / "test.csv"
        csv_file.write_text("a,b,c\n1,2,3\n4,5,6\n", encoding="utf-8")

        df = load_dataset(csv_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 3))
        self.assertEqual(list(df.columns), ["a", "b", "c"])

    def test_load_nonexistent_file_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            load_dataset("non_existent_path.csv")

    def test_unsupported_format_raises_error(self):
        dummy_file = self.tmp_path / "test.xyz"
        dummy_file.write_text("dummy content", encoding="utf-8")
        with self.assertRaises(ValueError):
            load_dataset(dummy_file)


if __name__ == "__main__":
    unittest.main()
