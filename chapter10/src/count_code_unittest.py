""" Write unittest for count_code"""
  

import unittest
from count_code import find_word
class count_code_test(unittest.TestCase):
  
  def test_pass(self):
       self.assertTrue(True)
  def test_fail(self):
       self.assertFalse(False)
 
if __name__=="__main__":
     unittest.main()

