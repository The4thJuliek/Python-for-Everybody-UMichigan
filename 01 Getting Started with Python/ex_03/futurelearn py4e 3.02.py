# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:41:27 2020

@author: ragini.m
"""

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5

hrs = input("Enter Hours:")
rate = input("rate per hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print ("ERROR!")
    quit()

Pay = h * r
overtime = (r * 1.5) + r
overpay = Pay + overtime

if h > 40:
    print (overpay)
else:
    print (Pay)