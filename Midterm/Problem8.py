#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 01:16:47 2017

@author: joshua
"""

# Midterm Problem 8

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    ourList = L
    index = 0
#    for i in L:
#        try:
#            if g(f(i)) == False:
#                print('deleted', i)
#                del i
#        except:
#            print('Except error deleted', i)
#            del i
        

    for i in range(len(ourList)-1,-1,-1):
        try:
            if not g(f(L[i])):
                del L[i]
#                del ourList[ourList.index(L[i])]
        except:
            del L[i]
#            del ourList[ourList.index(L[i])]
    if len(L) == 0:
        return -1
    else:
        return max(L)








def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4,"",'as',None]
print(applyF_filterG(L, f, g))
print(L)