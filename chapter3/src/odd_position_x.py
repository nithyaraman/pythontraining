"""
@file        : odd_position_x.py
@Brief       : Write the program to replace the odd position string with 'X' on any strings.
@Authour     : NithyaRaman
"""
word=raw_input("enter some word:")
list1=[]
num=0
for var in word:
    if (num==0 or num%2==0):
       list1.append(var)
    else:
       list1.append('x')   
    num+=1
print list1
