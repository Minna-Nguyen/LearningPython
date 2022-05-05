import unittest
from main import validate_player_input
from main import ask_name

# python3 -m unittest test.test_ui


class Test_letter(unittest.TestCase):

    def test_validate_player_input(self):
        self.assertTrue(validate_player_input("l"))

        self.assertFalse(validate_player_input("lasd"))
        self.assertFalse(validate_player_input("123"))
        self.assertFalse(validate_player_input("1"))

    def test_ask_name(self):
        self.assertTrue(ask_name("Helena"))
        self.assertTrue(ask_name("Ty"))

        self.assertFalse(ask_name("123"))
        self.assertFalse(ask_name("1"))
        self.assertFalse(ask_name("helena"))
        self.assertFalse(ask_name("H B"))
        self.assertFalse(ask_name("öä1p23"))
        self.assertFalse(ask_name(" he  lena"))
        self.assertFalse(ask_name("a"))
        self.assertFalse(ask_name("A"))
