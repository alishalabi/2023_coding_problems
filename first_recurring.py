"""
Given a string, find the first recurring character

input = "abca"
output = "a"

input = "bcaba"
output "c"

input = "abc"
output = None
"""

sample = "bcaba"

def solution(input):
    seen = set()
    for char in input:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None

print(solution(sample))
print(solution("abc"))
