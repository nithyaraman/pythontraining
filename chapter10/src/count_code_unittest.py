""" Write unittest for count_code"""
  
import unittest
from count_code import find_word
class count_code_test(unittest.TestCase):

  def test_case1(self):
      word=find_word(str1="code")
      self.assertEqual(word,1)
  def test_case2(self): 
      word=find_word(str1="cozecore")
      self.assertEqual(word,2)
  def  test_case3(self):
      word=find_word(str1="12345$#")
      self.assertEqual(word,0)
if __name__=="__main__":
     unittest.main()

