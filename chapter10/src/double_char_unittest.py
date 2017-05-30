""" Write unittest for double_char."""

import unittest
from double_char import double_str
str1="nithya"
class double_chartest(unittest.TestCase):
   
    def test_pass(self):
        self.assertTrue(True)
    def test_fail(self):
       self.assertFalse(False)

if __name__=="__main__":
   unittest.main()
