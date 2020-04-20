# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:16:54 2020

@author: ragini.m
"""


#PYTHON PROGRAM TO FIND SUM OF ELEMENTS IN LIST
#Given a list of numbers, write a Python program to find the sum of all the elements in the list.

#    Input : list1 = [10, 20, 4]
#    Output : 20
#
#    Input : list2 = [20, 10, 20, 4, 100]
#    Output : 100

# =============================================================================
# #EXAMPLE #1:
# 
# # Python program to find sum of elements in list 
# #total = 0
# 
# # creating a list 
# #list1 = [11, 5, 17, 18, 23] 
# 
# ## Iterate each element in list and add them in variale total 
# #for ele in range(0, len(list1)): 
# #	total = total + list1[ele] 
# 
# ## printing total value 
# #print("Sum of all elements in given list: ", total) 
# 
# 
# #Output:
# 
# #Sum of all elements in given list:  74
# =============================================================================


# =============================================================================
# #EXAMPLE #2: USING WHILE() LOOP
# 
# ## Python program to find sum of elements in list 
# #total = 0
# #ele = 0
# 
# # creating a list 
# #list1 = [11, 5, 17, 18, 23] 
# 
# ## Iterate each element in list and add them in variale total 
# #while(ele < len(list1)): 
# #	total = total + list1[ele] 
# #	ele += 1
# 	
# ## printing total value 
# #print("Sum of all elements in given list: ", total) 
# 
# 
## Output:
# 
## Sum of all elements in given list:  74
# 
# =============================================================================


# =============================================================================
# #EXAMPLE #3: RECURSIVE WAY
# 
# ## Python program to find sum of all elements in list using recursion 
# 
# ## creating a list 
# #list1 = [11, 5, 17, 18, 23] 
# 
# ## creating sum_list function 
# #def sumOfList(list, size): 
# #if (size == 0): 
# #	return 0
# #else: 
# #	return list[size - 1] + sumOfList(list, size - 1) 
# 
# ## Driver code	 
# #total = sumOfList(list1, len(list1)) 
# 
# #print("Sum of all elements in given list: ", total) 
# 
# 
# ## Output:
#  
# ## Sum of all elements in given list:  74
# =============================================================================

# =============================================================================
# EXAMPLE #4: USING SUM() METHOD
# 
# # Python program to find sum of elements in list 
# 
# ## creating a list 
# #list1 = [11, 5, 17, 18, 23] 
# #
# ## using sum() function 
# #total = sum(list1) 
# #
# ## printing total value 
# #print("Sum of all elements in given list: ", total) 
# 
# 
# # ## Output:
# #  
# # ## Sum of all elements in given list:  74
# =============================================================================

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)