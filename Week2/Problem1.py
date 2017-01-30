#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:17:38 2017

@author: joshua
"""

#def remBal(balance, annualInterestRate, monthlyPaymentRate):
"""
Function takes 3 inputs, balance, annual interest rate, and monthly payment rate.
Function will iterate through 1 year and return remaining balance after minimum monthly payments are calcualted.   
"""
# assign variables for readability
b = balance
annInt = annualInterestRate
monPay = monthlyPaymentRate

pBal = b

# calculate monthly interest rate
monInt = annInt / 12

# loop through each month and calculate payments
for month in range(0,12):
    minMon = monPay * pBal # minimum monthly payment
    b = pBal - minMon # new balance after payment made
    b += b*monInt # new balance after charging interest
    pBal = b # assign previous balance for next month iteration
    
# return Reamining Balance    
print("Remaining Balance:",round(b,2))