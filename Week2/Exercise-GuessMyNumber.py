#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 18 11:46:23 2017
#
#@author: joshua
#"""

high = 100
low = 0
cont = ''
print('Please think of a number between 0 and 100!')

while True:
    ans = (high + low)//2
    print("Is your secret number "+ str(ans) +"?")
    cont = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if cont == 'h':
        high = ans
    elif cont == 'l':
        low = ans
    elif cont == 'c':
        print('Game over. Your secret number was: ' + str(ans)) 
        break
    else:
        print('Sorry, I did not understand your input.')
        
