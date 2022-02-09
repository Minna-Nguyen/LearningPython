import unittest

from string_helper import get_title

class TestStringHelper(unittest.TestCase):
    def test_get_title(self):
        
        test_title1 = """
------------------------------
-         Battleship         -
------------------------------
            """.strip() # strip() will remove extra enters (\n} from start and end.

        self.assertEqual(get_title("battleship", 30, "-"), test_title1)
       
        test_title2 = """
****************************************
*            Palindrome App            *
****************************************
            """.strip()

        self.assertEqual(get_title("palindrome app", 40, "*"), test_title2)
    
        test_title3 = """
-----
-abc-
-----
""".strip()

        self.assertEqual(get_title("abc",3, "-"), "Invalid values, title length cannot be equal to graph length or be greater than graph lenght")
