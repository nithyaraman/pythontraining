"""
@File        : list_function.py
@Brief       : Use list functions append(), count(), extend(), index(), insert(), pop(), remove(), reverse() and sort()
@Authour     : Nithyaraman
"""
print"####Program using list function####"
print"1.append()"
list1 = ['1', '2', '3']
print list1
number = int(input("how many elements to appen"))
count = 0
while(count < number):
    list1.append(raw_input("enter element:"))
    count += 1
print list1
print "list is appended successfull"
print"\n\n2.count()"
object = raw_input("from the about list which you need to count?")
count_obj = list1.count(object)
print"it is present in %d times" % count_obj
print"no. of object counted successfully"
print "\n\n3.extend()"
number = int(input("how many elements to expand"))
counts = 0
while(counts < number):
    list1.extend(raw_input("enter element:"))
    counts += 1
print list1
print "list is extended successfully"
print "\n\n3.index()"
index_obj = raw_input("which element position want to know in about list")
if index_obj not in list1:
    print " it is not presented in above list"
else:
    position = list1.index(index_obj)
    print "element located on position", position

print "\n\n4.insert()"
insert_obj = raw_input("enter the element you want to insert:")
obj_position = int(input("enter the position you want to insert:"))
list1.insert(obj_position, insert_obj)
print list1
print "element is inserted successfully"
print "\n\n5.pop"
pop_num = int(input("how many element you need to pop"))
num = 0
while(num < pop_num):
    list1.pop()
    num += 1
print list1
print "successfully %d element poped" % pop_num
print "\n\n6.remove()"
rm_obj = (raw_input("above list which you want to remove"))
if rm_obj not in list1:
    print "object is not there"
else:
    list1.remove(rm_obj)
    print "object successfully removed"
print "list=", list1
print "\n\n7.revers"
list1.reverse()
print list1
print "list reversed successfully"
print "\n\n8.sort"
list1.sort()
print list1
print "list sorted successfully"
