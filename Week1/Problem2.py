# Problem 2
# Python 3.5
# Find how many times 'bob' occurs in the string

# Test string
s = 'slkasjlhwebobal;skdhowubobobalskhe' # 3 appearances

# ----------------------copy below this line -----------------------
total = 0
for l in range(0,len(s)):
    while l <= (len(s)-2):
        if s[l] == 'b' and s[l+1] == 'o' and s[l+2] == 'b':
            total += 1
            break
        else:
            break
print(total)
