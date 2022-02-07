import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
        self.assertEqual(is_name("Ville Virtanen"), True)

        # but if the function just returns True or False, it may be easier
        # to use assertTrue of assertFalse:
        self.assertTrue(is_name("Ville Virtanen"))
        self.assertFalse(is_name("ville virtanen"))
        self.assertFalse(is_name("12Villa"))
        self.assertFalse(is_name("ville"))

        # task number 3:
        self.assertTrue(is_name("ville virtanen", ignore_case=True))
        self.assertFalse(is_name("ville virtanen", ignore_case=False))
        self.assertTrue(is_name("Ville Virtanen", ignore_case=False))
        