# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:19:29 2020

@author: ragini.m
"""

score = input("Enter score: ")
sc = float(score)

try:
    if sc >= 0.9:
        print ("A")
    elif sc >= 0.8 <= 0.9:
        print ("B")
    elif sc >= 0.7 <= 0.8:
        print ("C")
    elif 0.7 >= sc >= 0.6:
        print ("D")
    elif sc < 0.6:
        print ("F")
except:
    sc > 1.0
    print ('Error')
    quit()