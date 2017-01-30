#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:10:35 2017

@author: joshua
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    while aStr != '':
        if char == aStr[0] or char == aStr[-1]:
            return True
        else:
            aStr = aStr[1:-1]
            return isIn(char,aStr)
    return False