# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 02:41:20 2020

@author: ragini.m
"""

10.2 
#Write a program to read through the mbox-short.txt and figure out the distribution 
#by hour of the day for each of the messages. You can pull the hour out from the 
#'From ' line by finding the time and then splitting the string a second time using a colon.

# =============================================================================
# #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# =============================================================================

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#Desired Output:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    time = line[0]
    counts[time] = counts.get(time, 0) + 1

x = sorted(counts.items())
  
lst = list(x)

for v,k in (lst):
    print (v,k)







