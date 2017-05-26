"""Read the CSV file and print it"""

import csv
import sys


# while run give "python filename.py <file name which need to read>"


file1 = csv.reader(open(sys.argv[1]))
for x in file1:
    print x
