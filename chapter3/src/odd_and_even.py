""" Print the odd and even number from list"""


list1 = [1,2,3,4,5,6,7,8,9]
print "given list is =", list1

odd_list = []
even_list = []

for var in list1:
    num = int(var)
    if num % 2 is 0:
        even_list.append(var)
    else:
        odd_list.append(var)

print "even number from the list =", even_list
print "odd number from the list =", odd_list
