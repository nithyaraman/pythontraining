""" Create the CSV with 10 columns and 10 rows"""

import csv
wtr = csv.writer(open("file1.csv", 'w'), delimiter=" ")

i = 0
while i < 10:
    wtr.writerow("0123456789")
    i += 1
