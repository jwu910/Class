#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:54:46 2017

@author: joshua
"""
# Topic: Bisection Searching

balance = 320000
annualInterestRate = 0.2

# Expected result 29157.09

remBal = balance # using Test Case
monInt = annualInterestRate / 12 
maxIter = 15
monLow = remBal / 12
monHigh = (remBal * ((1 + monInt)**12)) / 12.0
monMid = (monLow + monHigh) / 2.0
TOL = .01
counter = 0

print(remBal, monLow, monHigh, TOL)
while abs((monMid * 12)-balance) >= TOL:
#while counter <= maxIter:
    monMid = 0.5 * (monLow + monHigh)
    print('counter =',counter)
    print('Low =',monLow)
    print('MId =',monMid)
    print('high =',monHigh)
    if monMid == 0 or abs((monHigh - monLow) / 2.0) <= TOL:
        print(round(monMid,2))
        
    if monMid*12 > remBal:
        print("monMid = ", monMid*12)
        monLow = monMid
    else:
        monHigh = monMid
    counter += 1
    if counter > maxIter:
        break
    
print(monMid)