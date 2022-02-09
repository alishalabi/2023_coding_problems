"""
Given sorted array , return two numbers that add up to target value
"""

input1 = [1, 2, 3, 9, 10, 12] # None
input2 = [1, 1, 2, 2, 3, 4, 4, 6, 8, 9, 12] # (4, 4)
target = 8

# Method one
def find_pair(input, tar):
    for index in range(len(input) - 1):
        compliment = tar - input[index] # 7
        pointer = index # 0
        while pointer >= 0 and pointer < len(input) - 1:
            if input[pointer] == compliment:
                return (input[index], input[pointer])
            if input[pointer] > compliment:
                if input[pointer] >= tar:
                    break
                pointer -= 1
            if input[pointer] < compliment:
                pointer += 1
    return None


print(find_pair(input2, target))
print(find_pair(input1, target))
