"""Write the program to convert all the 
elements of list into string"""


list1 = []
print "empty list create", list1
number = int(input("enter how many elements need to insert in list"))
count = 0

while (count < number):
    list1.append(raw_input("enter element :"))
    count += 1

print "list are =", list1
print "by converting this list as string we get"

string1 = ''.join(list1)
print string1
