# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:33:43 2020

@author: ragini.m
"""

#7.1
#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt

file = input('Enter a file name: ')
opfile = open(file)
inp = opfile.read()
upfile = inp.upper()
upfile = upfile.strip()
print (upfile)
