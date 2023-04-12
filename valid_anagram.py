"""
Given two strings s1 and s2, check to see if they are anagrams
"""

# Assumption 1: all input lower case (use a .lower() function if not)
# Assumption 2: all chars in input (ie no digits)

s1 = "dangerd"
s2 = "rangedd"
s3 = "applepp"
s4 = "abcdefghijklmnop"

def is_valid(string1, string2):
# early exits (not same length)
    if len(string1) != len(string2):
        return False
# convert string 1 into dictionary, convert string 2 into dictionary
    dictionary1 = {}
    dictionary2 = {}
    for char in string1:
        if char in dictionary1:
            dictionary1[char] += 1
        else:
            dictionary1[char] = 1

    for char in string2:
        if char in dictionary2:
            dictionary2[char] += 1
        else:
            dictionary2[char] = 1
    # compare two dictionaries
    if dictionary1 == dictionary2:
        return True
    else:
        return False

print(is_valid(s1, s2))
print(is_valid(s1, s3))
print(is_valid(s3, s4))
