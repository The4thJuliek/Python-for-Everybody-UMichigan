# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:15:24 2020

@author: ragini.m
"""

#6.5 
#Write code using find() and string slicing (see section 6.10) 
#to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.
#
#Desired Output : 0.8475

text = "X-DSPAM-Confidence:    0.8475";

spcpos = text.find(" ")
endpos = text.find("5")

finpos = (text[19:29])
fltpos = float(finpos)
print (fltpos)




#DISREGARD BELOW (RETAIN FOR REFERENCE)

#upd_finpos = finpos.lstring()
#print (upd_finpos)
#fltpos = float(upd_finpos)
#print (fltpos)