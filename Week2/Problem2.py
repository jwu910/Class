#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:58:12 2017

@author: joshua
"""

"""
balance
annualInterestRate
"""

# Test cases
balance = 3926
annualInterestRate = 0.2
preBal = balance

monInt = annualInterestRate / 12 # monthly interest rate
minFixPay = 0

while preBal > 0:
    minFixPay += 10
    preBal = balance
    for month in range(0,12):
        monUnPaid = preBal - minFixPay # Monthly unpaid balance
        preBal = monUnPaid + (monUnPaid * monInt) # update balance
print(minFixPay)
