# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:00:39 2020

@author: ragini.m
"""

#5.2 
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and 
#put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below.
#  
# 
largest = None
smallest = None
largest_so_far = 0
smallest_so_far = 0
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        n = int (num)
        for itervar in [n]:
            if largest is None or itervar > largest :
                 largest = itervar
        for itervar in [n]:
            if smallest is None or itervar < smallest:
                smallest = itervar
    except:
        if num == ("bob"):
            print ('Invalid input')   
            
print("Maximum is", largest) 
print("Minimum is", smallest)