"""
@file    : double_char.py
@Brief   : Given a string, return a string where for every char in the original, there are two chars
@Authour : NithyaRaman
"""
def double_str(str1): 
   list1=list(str1)
   length=len(list1)
   i=0
   while(i < 2*length):
       list1.insert(i,list1[i])
       i+=2
   str2=''.join(list1)
   return str2 

str3=raw_input ("enter your string:")
str4=double_str(str3)
print str4
