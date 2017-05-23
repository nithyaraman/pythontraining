""" Write a program to count no of lines in a text file """

#open a file
fo=open("newfile.txt",'w+')



#write in file
lines=""
number=int(raw_input("enter number of lines\n>"))

for i in xrange(number):
   lines+=raw_input()+"\n"

fo.write(lines)
fo.close()



#count number of lines
num_lines=0

for i in open("newfile.txt"):
   num_lines+=1

print "number of line is :",num_lines



#count number of words and letters
newfile=""

with open("newfile.txt") as newfile:
   r=newfile.read()
   word=r.split()

num_word=0
num_letter=0

for i in word:
   for letter in i:
      num_letter+=1
   num_word+=1

print "number of words in file:",num_word
print "number of letters in file:",num_letter
