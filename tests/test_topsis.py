import unittest
import numpy as np
from topsis.topsis import topsis

class TestTopsis(unittest.TestCase):
    def test_topsis(self):
        data = np.array([
            [250, 16, 12, 5],
            [200, 16, 8, 3],
            [300, 32, 16, 4],
            [275, 32, 8, 4],
            [225, 16, 16, 2]
        ])
        weights = [0.25, 0.25, 0.25, 0.25]
        impacts = ['+', '+', '-', '+']
        result = topsis(data, weights, impacts)
        self.assertAlmostEqual(result[0], 0.5344, places=4)

if __name__ == '__main__':
    unittest.main()
