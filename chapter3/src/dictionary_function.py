"""
@File       : dictionay_function.py
@Brief      : Practice with dictionary functions functions clear(), get(), has_key(), items(), keys(), pop(),
            popitem(), update(), values()
@Authour    : NithyaRaman
"""
print "\n1.clear()"
print "this function remove all values of dictionary"
dict1={'1':'one','2':'two','3':'three' }
print "dictionary has =",dict1 
print "by clear the elements all entries can remove"
dict1.clear()
print dict1
print "\n\n2.get()"
dict1={1:'one',2:'two',3:'three' }
print "dictionary has =",dict1
number=int(input("select one key in dictionary:"))
if number not in dict1:
    print "that key is not available"
else:
    print dict1.get(number)
print "\n\n3.has_key()"
print "enter key to know is there or not"
key_num=int(input("enter key:"))
print dict1.has_key(key_num)
print "\n\n4.items()"
print "return list of dictionary"
print dict1.items()
print "\n\n5.keys()"
print "keys in dictionary"
print dict1.keys()
print "\n\n6.values()"
print "values in dictionary"
print dict1.values()
print "\n\n7.pop()"
pop_key=int(input("enter key which you want to pop:"))
if pop_key not in dict1:
     print "that key is not available"
else:
     dict1.pop(pop_key)   
print dict1
print "\n\n8.popitem()"
dict1.popitem()
print dict1
print "\n\n9.update()"
dict2={'100':'hundred', '200':'twohundred'}
print dict2
print "dictionary updated with above"
dict1.update(dict2)
print dict1

