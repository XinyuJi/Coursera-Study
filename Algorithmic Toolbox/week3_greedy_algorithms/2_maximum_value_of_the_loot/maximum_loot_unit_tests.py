import unittest
from maximum_loot import maximum_loot_value


class TestMaximumLoot(unittest.TestCase):
    def test(self):
        for (capacity, weights, prices, answer) in [
            (50, [20, 50, 30], [60, 100, 120], 180.0),
            (10, [30], [500], 500/3),
            (100, [20, 50, 30], [60, 100, 120], 280.0),
            (1000, [10], [20], 20),
            (1000, [500], [30], 30)
        ]:
            self.assertAlmostEqual(
                maximum_loot_value(capacity, weights, prices),
                answer,
                delta=1e-03
            )


if __name__ == '__main__':
    unittest.main()
