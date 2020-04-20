# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:50:00 2020

@author: ragini.m
"""

#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
#Once "done" is entered, print out the total, count, and average of the numbers. 
#If the user enters anything other than a number, detect their mistake using 
#try and except and print an error message and skip to the next number.
#
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333

num = 0
total = 0

while True:
    num = input('Enter a number:')
    if num == ('done'):
        break
    try:
        n = float(num)   
    except:
        print ('Invalid Input!')
        continue
    print (n)
    n = n + 1
    total = total + n
    
print (total, n, total/n)