"""Do the basic linux commands operatios using sys"""


import sys


def printargv():
    count = 0
    for loop in sys.argv:
        print "argument%d=%s" % (count, loop)
        count += 1
    return


def countargv():
    count = len(sys.argv)
    print "length of argument is ", count
    return


num = int(input("choose\n1.print arg\n2.count arg\n="))

if num is 1:
    printargv()

if num is 2:
    countargv()
