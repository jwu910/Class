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
maxIter = 30
monLow = remBal / 12
monHigh = (balance * ((1 + monInt)**12)) / 12.0
monMid = (monLow + monHigh) / 2.0
TOL = .01
counter = 0

while counter < maxIter:
    monMid = (monLow + monHigh)/2.0
    for i in range(12):
        remBal -= monMid
        remBal = remBal + (remBal * monInt)
    if remBal == 0 or (monLow+monHigh)/2 < TOL:
        print(monMid)
        break
    if remBal > 0:
        monLow = monMid
        remBal = balance
    else:
        monHigh = monMid
        remBal = balance
        
    counter += 1
    #print('not found, checking again',counter)
    
print(round(monMid,2)) 
    
    


"""
while preBal > 0:
    minFixPay += 10
    preBal = balance
    for month in range(0,12):
        monUnPaid = preBal - minFixPay # Monthly unpaid balance
        preBal = monUnPaid + (monUnPaid * monInt) # update balance
print(minFixPay)
"""
