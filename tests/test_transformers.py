"""Unit tests for custom feature transformers."""

import unittest
import pandas as pd
from datascience_toolbox.features.transformers import OutlierCapper


class TestTransformers(unittest.TestCase):
    def test_outlier_capper(self):
        data = {"val": [10, 11, 12, 11, 10, 12, 100, -50]}
        df = pd.DataFrame(data)

        capper = OutlierCapper(factor=1.5)
        capper.fit(df)
        transformed = capper.transform(df)

        self.assertLess(transformed["val"].max(), 100)
        self.assertGreater(transformed["val"].min(), -50)


if __name__ == "__main__":
    unittest.main()
