""" Write a program to count no of lines in a text file """

# open a file
fo = open("newfile.txt", 'w+')


# write in file
lines = ""
number = int(raw_input("enter number of lines\n>"))

for i in xrange(number):
    lines += raw_input() + "\n"

fo.write(lines)
fo.close()


# funtion count number of lines
def countline(filename):
    num_line=0
    with open (filename,'r') as files:
        for i in files:
           num_line+=1
    return num_line


#function call to count line
numline=countline("newfile.txt")
print "number of line is :", numline


# count number of words and letters
newfile = ""

with open("newfile.txt") as newfile:
    r = newfile.read()
    word = r.split()

num_word = 0
num_letter = 0

for i in word:
    for letter in i:
        num_letter += 1
    num_word += 1

print "number of words in file:", num_word
print "number of letters in file:", num_letter
