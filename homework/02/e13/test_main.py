import unittest

from main import calculate_sum, get_max
class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(3,4), 7)

    def test_get_max(self):
        self.assertEqual(get_max(1,2,3), 3)
        self.assertEqual(get_max(1,1,1), 1)
        self.assertEqual(get_max(0,1,-1), 1)
        self.assertEqual(get_max(-12,9,1), 9)
        self.assertEqual(get_max(1,1,5), 5)
        self.assertEqual(get_max(-11,-1,0), 0)
        self.assertEqual(get_max(-1,-2,-3), -1)
