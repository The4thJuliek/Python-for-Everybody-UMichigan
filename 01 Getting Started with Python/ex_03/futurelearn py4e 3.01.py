# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:23:38 2020

@author: ragini.m
"""
hrs = input("Enter Hours:")
rate = input("rate per hour:")
h = float(hrs)
r = float(rate)
Pay = h * r
overtime = (r * 1.5) + r
overpay = Pay + overtime

if h > 40:
    print (overpay)
else:
    print (Pay)