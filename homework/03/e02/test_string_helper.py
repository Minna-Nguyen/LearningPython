import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
        self.assertEqual(is_name("Ville Virtanen"), True)

        # but if the function just returns True or False, it may be easier
        # to use assertTrue of assertFalse:
        self.assertTrue(is_name("Ville Virtanen"))
        self.assertFalse(is_name("testi nimi"))
        self.assertFalse(is_name("testi Nimi"))
        self.assertFalse(is_name("Testi nimi"))
        self.assertFalse(is_name("12 nimi"))
        self.assertFalse(is_name("123 123?="))
        self.assertFalse(is_name("VilleVirtanen"))

        self.assertFalse(is_name("12Villa"))
        self.assertFalse(is_name("ville"))
        self.assertFalse(is_name("Honney"))
        self.assertFalse(is_name(" ville"))
        self.assertFalse(is_name(" Melissa"))
        self.assertFalse(is_name("mille "))
        # self.assertFalse(is_name(" Viii Mooi "))
        # self.assertFalse(is_name(" Viii Mooi"))
        # self.assertFalse(is_name("Viii Mooi "))
        self.assertFalse(is_name("?? Hello"))
