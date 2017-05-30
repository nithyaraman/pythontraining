""" Write unittest for double_char."""

import unittest
from double_char import double_str
class double_chartest(unittest.TestCase):
   def test_letter(self):
       word=double_str("nithya")    
       self.assertEqual(word,"nniitthhyyaa")
   def test_number(self):
       word=double_str("123")
       self.assertEqual(word,"112233")
   def test_spl_symbol(self):
       word=double_str("@#$%") 
       self.assertEqual(word,"@@##$$%%")
 
if  __name__=="__main__":
   unittest.main()
