"""Get the 5 numbers from command line and do the basic arithmetic 
operations. First argument should be like'add', 'mul'. Do the
 operations based first argument word."""


# while running give 
#"python <filename> add 1 2 3 4 5"(add followed by any numbers) or 
#"python <filename> mul 1 2 4 5 3"(mul followed by any numbers)

import sys


def add(*arg):
  num=0
  for x in arg:
     for y in x :
        y=int(y)
        num+=y
  return num



def mul(*arg):
   num=1
   for x in arg:
      for y in x:
          y=int(y)
          num*=y
   return num




if sys.argv[1]=='add':
  total=add(sys.argv[2:])
  print "total=",total 
 

if sys.argv[1]=='mul':
   total= mul(sys.argv[2:])
   print "total=",total
