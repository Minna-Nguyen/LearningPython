import unittest

from validation import is_name
from string_helper import csv_to_list

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(is_name("Ville"))
        self.assertTrue(is_name("Virtanen"))
        self.assertTrue(is_name("Heli-Virtanen"))
        self.assertFalse(is_name("testi nimi"))
        self.assertFalse(is_name("testi Nimi"))
        self.assertFalse(is_name("Testi nimi"))
        self.assertFalse(is_name("12 nimi"))
        self.assertFalse(is_name("123 123?="))
        self.assertFalse(is_name("VilleVirtanen"))

        self.assertFalse(is_name("12Villa"))
        self.assertFalse(is_name("ville"))
        self.assertFalse(is_name(" ville"))
        self.assertFalse(is_name(" Melissa"))
        self.assertFalse(is_name("mille "))
        self.assertFalse(is_name(" Viii Mooi "))
        self.assertFalse(is_name(" Viii Mooi"))
        self.assertFalse(is_name("Viii Mooi "))
        self.assertFalse(is_name("M N"))

        self.assertFalse(is_name("?? Hello"))
        self.assertFalse(is_name("ville virtanen"))
        self.assertFalse(is_name("ville virtanen"))
        self.assertFalse(is_name("123 virtanen"))
        self.assertFalse(is_name("ville 12!dew"))
        self.assertFalse(is_name("123 virtanen"))
        self.assertFalse(is_name("ville 12!dew"))
        self.assertFalse(is_name("VilleVirtanen"))
        self.assertFalse(is_name("12Villa"))
        self.assertFalse(is_name("ville"))
        
        self.assertFalse(is_name("12Villa"))
        self.assertFalse(is_name("ville"))
        self.assertFalse(is_name(" ville"))
        self.assertFalse(is_name(" Melissa"))
        self.assertFalse(is_name("Melissa "))
        self.assertFalse(is_name("mille "))
        self.assertFalse(is_name(" Viii Mooi "))
        self.assertFalse(is_name(" Viii Mooi"))
        self.assertFalse(is_name("Viii Mooi "))
        self.assertFalse(is_name(" ville"))
        self.assertFalse(is_name(" Melissa"))
        self.assertFalse(is_name("mille "))
        self.assertFalse(is_name(" Viii Mooi "))
        self.assertFalse(is_name(" Viii Mooi"))
        self.assertFalse(is_name("Viii Mooi "))

        self.assertFalse(is_name("ville-balle mobil-lenn"))
        self.assertFalse(is_name("ville-Bille Mobil-alaa"))
        self.assertFalse(is_name("Ville-bille Mobil-alaa"))
        self.assertFalse(is_name("Ville-bille Mobil hels"))
        self.assertFalse(is_name("Ville-bille Mobil hels"))

class TestValidation(unittest.TestCase):
    def test_csv_to_list(self):
        self.assertTrue(csv_to_list("1,Minna,Hello\n2,Miten,Menee"))
        self.assertTrue(csv_to_list("1,Minna,Hello"))
        self.assertRaises(Exception, csv_to_list, int)
        self.assertRaises(Exception, csv_to_list, list())
        self.assertRaises(Exception, csv_to_list, tuple())
        self.assertRaises(Exception, csv_to_list, set())
        self.assertRaises(Exception, csv_to_list, dict())
