#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:24:43 2017

@author: joshua
"""

# Midterm Problem 7

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    index = 0
    dd1 = {}
    dd2 = {}
    while index <= (len(d1)+len(d2)):
        if index in d1 and index in d2:
            dd1[index] = f(d1[index],d2[index])
            index += 1
        elif index in d1 and index not in d2:
            dd2[index] = d1[index]
            index += 1
        elif index in d2 and index not in d1:
            dd2[index] = d2[index]
            index += 1
        else:
            index += 1
    result = (dd1,dd2)
    return result
    
    
# ________ Function F() is defined by the Grader. Do not Copy below this line _________ 
def f(d1,d2):
    return d1+d2
    