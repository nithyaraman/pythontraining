""" Calculating sum of numbers from 1-100 using reduce()"""

print "sum of number between the range"
start = int(input("start with:"))
end = int(input("end with:"))


result = reduce(lambda x, y: x + y, range(start, end))
print result
