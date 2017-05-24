""" Write a program to count no of lines in n no of text files
 and Plot it as a bar graph as File vs Lines """

import matplotlib.pyplot as plt
import os
import numpy as np

file_list = []
line_list = []

for filename in os.listdir("filesdir"):
    file_list.append(filename)

    filepath = "/home/nithya/pythontraining/chapter5/src/filesdir/" + filename
    fo = open(filepath, 'r+')

    num_line = 0

    for i in open(filepath):
        num_line += 1
    line_list.append(num_line)

xaxis = file_list
x_pos = np.arange(len(xaxis))
plt.xticks(x_pos, xaxis)

yaxis = line_list

plt.xlabel("file list")
plt.ylabel("number of lines")
plt.title("files vs lines")

plt.bar(x_pos, yaxis)
plt.show()
