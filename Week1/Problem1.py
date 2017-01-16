# Python 3.5
# Find the Vowels

s = input("type string = ")
vowels = 0
for letter in s:
	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
		vowels += 1
print(vowels)
