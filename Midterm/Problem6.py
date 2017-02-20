#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:17:04 2017

@author: joshua
"""

# Midterm Problem 6
# L = [[1, 2], [3, 4], [5, 6, 7]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for item in L:
        item.reverse()
    
    return L