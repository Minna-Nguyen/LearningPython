import unittest
from e09 import reverse
from e11 import is_palindrome

class Test_e14(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("hello"),"olleh")
        self.assertEqual(reverse("this"),"siht")
        self.assertEqual(reverse("what"),"tahw")
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("sas", lowercase=True), True)
        self.assertEqual(is_palindrome("Dna", lowercase=True), True)
        self.assertEqual(is_palindrome("MOM", lowercase=True), True)
        self.assertEqual(is_palindrome("anD", lowercase=True), True)
        self.assertEqual(is_palindrome("123", lowercase=True), False)
        self.assertEqual(is_palindrome("hello how are you?", lowercase=True), False)