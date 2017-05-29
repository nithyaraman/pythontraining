"""Create the dictionary dict_sample = {1:1, 2:2} using dictionary comprehension"""


def createdict(x, y):
    dict1 = {n: n for n in range(x, y)}
    print dict1
    return


print "create a dictionary"
start = int(input("start with"))
end = int(input("end with"))
createdict(start, end)
