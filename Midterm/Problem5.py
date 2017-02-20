#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:10:42 2017

@author: joshua
"""

# Midterm Problem 5

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    index = 0
    sumTot = 0
    for index in range(len(listA)):
        sumTot += (listA[index] * listB[index])
    return sumTot