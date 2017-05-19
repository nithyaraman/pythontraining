"""
@file     : create_tuple.py
@Brief    : Create one tuple and print the elements of tuple
@Authour  : NithyaRaman
"""
tuple1 = ()
list1 = []
print "empty tuple created", tuple1
number = int(input("enter how many element need to add"))
count = 0
while (count < number):
    list1.append(raw_input("enter element"))
    count += 1
tuple1 = tuple(list1)
print tuple1
