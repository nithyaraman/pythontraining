""" Write a program to count no of lines in n no of text files
 and Plot it as a bar graph as File vs Lines """

import matplotlib.pyplot as plt
import os
import numpy as np
import count


file_list = []
line_list = []


for filename in os.listdir("filesdir"):
    file_list.append(filename)


#use count module to count lines in files
    filepath = "/home/nithya/pythontraining/chapter5/src/filesdir/" + filename
    fo = open(filepath, 'r+')
    num_line=count.countline(filepath)
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
