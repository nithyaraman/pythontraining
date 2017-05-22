"""Write the program to remove the duplicate elements from list"""


list1 = []
print "empty list created", list1
number = int(input("enter number of element need to insert"))
count = 0

while (count < number):
    list1.append(raw_input("enter element:"))
    count += 1

print "list =", list1
num = -1

while(num < len(list1)):
    count = list1.count(list1[num])
    if count != 1:
        del list1[num]
    num += 1

print list1
print "duplicates removed in list successfully"
