"""
@file           : Print_letter.py
@Brief          : Print the letters from 'gnu-linux is rule the world now'
@Authour        : NithyaRaman
"""
import string
string="gnu-linux is rule the world now"
print "length of full string",len(string)
letter=[]
space=0
spl_symbol=0
for var in string:
   if str.isalpha(var):
      letter.append(var)
   elif str.isspace(var):
       space+=1 
   else: 
       spl_symbol+=1
print "number of letter %d"%len(letter)
print "number of space %d"%space
print "number of spl_chac %d"%spl_symbol
print "letter which is inside is",''.join(letter)

