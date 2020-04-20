# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 04:14:30 2020

@author: ragini.m
"""

#7.2 Write a program that prompts for a file name, then opens that file and
#reads through the file, looking for lines of the form:
#
#X-DSPAM-Confidence:    0.8475
#
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#
#Desired Output - Average spam confidence: 0.750718518519

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line[20::]
    if line.find('\n'):
        line.strip('\n')
    line = float(line)
    count += 1
    total += line

print ("Average spam confidence:", total/count)
