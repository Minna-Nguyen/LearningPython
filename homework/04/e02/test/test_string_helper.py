import unittest

from string_helper import is_name, list_to_str

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
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
        self.assertFalse(is_name(" Viii Mooi "))
        self.assertFalse(is_name(" Viii Mooi"))
        self.assertFalse(is_name("Viii Mooi "))
        self.assertFalse(is_name("M N"))

        self.assertFalse(is_name("?? Hello", ignore_case=True))
        self.assertFalse(is_name("?? Hello", ignore_case=False))
        # task number 3:
        self.assertTrue(is_name("ville virtanen", ignore_case=True))
        self.assertFalse(is_name("ville virtanen", ignore_case=False))
        self.assertTrue(is_name("Ville Virtanen", ignore_case=False))
        self.assertFalse(is_name("123 virtanen", ignore_case=False))
        self.assertFalse(is_name("ville 12!dew", ignore_case=False))
        self.assertFalse(is_name("123 virtanen", ignore_case=True))
        self.assertFalse(is_name("ville 12!dew", ignore_case=True))
        self.assertFalse(is_name("VilleVirtanen", ignore_case=True))
        self.assertFalse(is_name("12Villa", ignore_case=True))
        self.assertFalse(is_name("ville", ignore_case=True))
        self.assertFalse(is_name("Honney", ignore_case=True))
        
        
        self.assertFalse(is_name("12Villa", ignore_case=False))
        self.assertFalse(is_name("ville", ignore_case=False))
        self.assertFalse(is_name("Honney", ignore_case=False))
        self.assertFalse(is_name(" ville", ignore_case=False))
        self.assertFalse(is_name(" Melissa", ignore_case=False))
        self.assertFalse(is_name("mille ", ignore_case=False))
        self.assertFalse(is_name(" Viii Mooi ", ignore_case=False))
        self.assertFalse(is_name(" Viii Mooi", ignore_case=False))
        self.assertFalse(is_name("Viii Mooi ", ignore_case=False))
        self.assertFalse(is_name(" ville", ignore_case=True))
        self.assertFalse(is_name(" Melissa", ignore_case=True))
        self.assertFalse(is_name("mille ", ignore_case=True))
        self.assertFalse(is_name(" Viii Mooi ", ignore_case=True))
        self.assertFalse(is_name(" Viii Mooi", ignore_case=True))
        self.assertFalse(is_name("Viii Mooi ", ignore_case=True))

        self.assertTrue(is_name("Ville-Bille Mobil", ignore_case=True))
        self.assertTrue(is_name("Ville-Bille Mobil", ignore_case=False))
        self.assertFalse(is_name("ville-balle mobil-lenn", ignore_case=False))
        self.assertTrue(is_name("Ville-Bille Mobil-Alaa", ignore_case=True))
        self.assertFalse(is_name("ville-Bille Mobil-alaa", ignore_case=False))
        self.assertFalse(is_name("Ville-bille Mobil-alaa", ignore_case=False))
        self.assertFalse(is_name("Ville-bille Mobil hels", ignore_case=False))
        self.assertFalse(is_name("Ville-bille Mobil hels", ignore_case=True))

    def test_list_to_str(self):
        self.assertTrue(list_to_str(["Minna Thao", "Nguyen Thanh"]))
        self.assertRaises(Exception, list_to_str,[])
        self.assertRaises(Exception, list_to_str,[123123, '?', '-&&&'])
        self.assertRaises(Exception, list_to_str,["Minna Thao", ""])
        self.assertRaises(Exception, list_to_str,({"Minna Thao", "Nguyen Thanh"}))
        self.assertRaises(Exception, list_to_str,({1:"Minna Thao", 2:"Nguyen Thanh"}))
        self.assertRaises(Exception, list_to_str,("Minna Thao", "Nguyen Thanh"))
