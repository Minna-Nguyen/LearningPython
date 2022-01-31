import unittest
def calculate_sum(count1, count2):
    sum = count1 + count2
    return sum

sum = calculate_sum(4,4)
print(sum)

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual("hello", "hello")
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)


