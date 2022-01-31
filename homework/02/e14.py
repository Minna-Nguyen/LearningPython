import unittest
from e09 import reverse
from e11 import isPalindrome

class Test_e14(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("hello"),"olleh")
        self.assertEqual(reverse("this"),"siht")
        self.assertEqual(reverse("what"),"tahw")
    
    def test_isPalindrome(self):
        self.assertEqual(isPalindrome("sas", lowercase=True), True)
        self.assertEqual(isPalindrome("Dna", lowercase=True), False)
        self.assertEqual(isPalindrome("MOM", lowercase=True), True)
        self.assertEqual(isPalindrome("anD", lowercase=True), False)
        self.assertEqual(isPalindrome("123", lowercase=True), False)
        self.assertEqual(isPalindrome("hello how are you?", lowercase=True), False)