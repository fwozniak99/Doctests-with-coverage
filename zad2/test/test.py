import unittest
from zad2.src.validpassword import Password

class ValidTest(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def test_is_long_enough(self):
        self.assertEqual(self.temp.ValidPassword("abc"), False)

    def test_correct_password(self):
        self.assertEqual(self.temp.ValidPassword("Password9$"), True)

    def test_no_special(self):
        self.assertEqual(self.temp.ValidPassword("Password99"), False)

    def tearDown(self):
        self.temp = None