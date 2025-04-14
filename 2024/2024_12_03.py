# Part 1

import re
# mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024
# example
# corupted_memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

corupted_memory = ''
with open("2024/additional_files/corrupted_memory.txt", "r") as f:
    for line in f:
        corupted_memory = corupted_memory + line
# print(corupted_memory)

# What do you get if you add up all of the results of the multiplications?

def sum_multiplications(list_of_pairs):
    sum = 0
    for pair in list_of_pairs:
        # removing braces and changing data type from string to integer
        a,b = [int(e) for e in pair.lstrip('mul(').rstrip(')').split(',')]
        # print(a)
        # print(b)
        sum += a*b
        # print('sum')
        # print(sum)
    return sum
# scanning uncorrupted multiplications
scanned = []
scanned = re.findall(r"(?:mul\()\d{1,3}[,]\d{1,3}(?:\))",corupted_memory)
adding_multiplications = sum_multiplications(scanned)
#print(scanned)
print(adding_multiplications)

# Part 2

