"""Print odd number between 1-100 using list comprehension"""


def oddnum(x, y):
    number = range(x, y)
    lst = [x for x in number if x % 2 == 1]
    print lst
    return


print "\tprinting odd number between range"
start = int(input("start from:"))
endwith = int(input("end with:"))
oddnum(start, endwith)
