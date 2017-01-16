# Problem 3
# Python 3.5

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Test string
s = 'abcedfghijklmnopqrstuvwxyz'
# s = 'a'
# ----------------------copy below this line -----------------------
longest = ''
temp = ''
if len(s) == 1:
    print('Longest substring in alphabetical order is:',s)
elif len(s) > 1:
    for i in range(0,len(s)-1):
        if s[i] <= s[i+1]:
            temp += s[i]
            if i == len(s)-2:                   # If letter is the last letter
                if s[i] >= s[i-1]:              # Check if letter is greater than preceeding
                    temp += s[i+1]              # If so, add letter to end of temp string
                if len(temp) > len(longest):    # If temp string is longer than longest string
                    longest = temp              # Replace longest with temp
                    temp = ''                   # Reset temp             
        elif s[i] > s[i+1]:
            temp += s[i]                        # Break process and add last letter in to temp string
            if len(temp) > len(longest):        # Check if length is longer than longest
                longest = temp
                temp = ''
            temp = ''
print('Longest substring in alphabetical order is:',longest)