"""Convert all the numbers between 1-100 as string using map"""

from num2words import num2words


print "convert number in to word"
start = int(input("start from:"))
end = int(input("end with:"))

list1 = map(lambda x: num2words(x), range(start, end))
print u",".join(list1)
