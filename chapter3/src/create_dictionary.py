""" Create the dictionary like{'one':1, ...... 'ten':10} 
and print it"""


list1 = ["one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten"]
list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

dict1 = {}
dict1 = dict(zip(list1, list2))

print dict1
