# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:42:01 2020

@author: ragini.m
"""

#Write a program to read through the mbox-short.txt and figure out who has sent 
#the greatest number of mail messages. 
 
 
#After the dictionary is produced, the program reads through the dictionary using a 
#maximum loop to find the most prolific committer.

#Desired Output: cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line, 0) + 1
    
bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print (bigWord, bigCount)