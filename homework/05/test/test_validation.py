import unittest
from validation import is_date

class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-02-16"))
        self.assertTrue(is_date("2022-12-31"))
        self.assertFalse(is_date("2001-16-02"))
        self.assertFalse(is_date("2001-16-021"))
        self.assertFalse(is_date("2001-166-01"))
        self.assertFalse(is_date("2001-02-33"))
        self.assertFalse(is_date("2001 12 33"))
        self.assertFalse(is_date("2001:12:33"))
        self.assertFalse(is_date("2001_12_33"))
        self.assertFalse(is_date("2001-02-33"))
        self.assertFalse(is_date("22-10-01"))
        self.assertFalse(is_date("-20-6-2"))
        self.assertFalse(is_date("2001-1-12"))
        self.assertFalse(is_date("2001-07-2"))
        self.assertFalse(is_date("2001-7-2"))
        self.assertFalse(is_date("2001"))
        self.assertRaises(Exception, is_date, int)
        self.assertRaises(Exception, is_date, tuple())
        self.assertRaises(Exception, is_date, dict())
        self.assertRaises(Exception, is_date, set())