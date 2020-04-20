# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:28:29 2020

@author: ragini.m
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


count = 0
sum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    nums = int(tag.contents[0])
    sum = sum + nums
    count += 1

print (count)
print (sum)
