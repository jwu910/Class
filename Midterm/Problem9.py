#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 00:00:19 2017

@author: joshua
"""

# Midterm Problem 9

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])
#    for i in aList:
#        if isinstance(i,list):
#            aList.replace(i,flatten(i))
#        else:
#            aList.replace(i,i)
            
            
    
    
print(flatten([[1], [1],[123,2,3,[1,2,5],[[12,12,5],12,2]]]))
#print(flatten([[3], [2, 1, 0], [4, 5, 6, 7]]))