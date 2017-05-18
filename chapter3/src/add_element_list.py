"""
@file        : add_element_list.py
@Brief       : Create the list and add the elements
@Authour     : NithyaRaman
"""
list1=[]
print "empty list is created ",list1
number=int(input("how many element you need to add"))
count=0
while(count<number):
   list1.append(raw_input("enter element:"))
   count+=1 
print list1
