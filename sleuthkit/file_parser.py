#!/usr/bin/python
#
# ************
# Author: Ryan MacLennan
# Filename: gui.py
# This file is to parse the output of the files from the commands
# and then to export to a pdf
# ************

import os

'''this should at some point have a directory of files in it
and then use those files to e run in the with statement.  Each file
will be the output of each command run with it's options.'''

titles = [[]]     # list of sections taken from the file
left_sections = []   # list of sections with in each main title
right_sections = []  #data for each left section
#data = []       # values for each section (should be same size as sections

with open(file_example) as f:
    count = 0
    for line in f:
        count++
        if line.contains(" "):
            insert_count = count + 1
        if count == insert_count or count == 0:
            titles.append(line.readline())
        if line.isupper() != True:
            left_sections.append(line.partition(":")[0])
            right_sections.append(line.partition(":")[2])



