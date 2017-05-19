"""
@File      : add_remove_update_dict.py
@Brief     : Write the program to add, remove and update elements in dictionary
@Authour   : NithyaRaman
"""
dict1 = {}
print "empty dictionary created", dict1
print "\n\n1.add"
number = int(input("how many elements need to add :"))
count = 1
while (count <= number):
    dict1[count] = raw_input("enter value:")
    count += 1
print dict1
print "\n\n2.remove"
print "above which you want to remove"
number = int(input("enter any of above key:"))
if number not in dict1.keys():
    print "that key alreaady not available"
else:
    del dict1[number]
print dict1
print "\n\n3.update"
dict2 = {100: 'hundred', 200: 'two hundred'}
print "another dict=", dict2
print "by update this with above dictionary"
dict1.update(dict2)
print dict1
