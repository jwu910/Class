# Problem 3
# Python 3.5

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Test string
s = 'abcdefg'
# s = 'a'
# ----------------------copy below this line -----------------------
index = 0
longest = ''
temp = ''
strings = []
print(s,len(s))
if len(s) == 1:
    print(s)
elif len(s) > 1:
    for i in range(0,len(s)-1):
        if s[index] <= s[index+1]:
            temp = temp + s[index]
            index += 1
        elif s[index] > s[index+1]:
            strings.append(temp)
            temp = ''
            index += 1
print(strings)