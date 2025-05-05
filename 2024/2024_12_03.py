# Part 1

import re
# mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024
# example
# corupted_memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

corupted_memory = ''
with open("2024/additional_files/corrupted_memory.txt", "r") as f:
    for line in f:
        corupted_memory = corupted_memory + line

# What do you get if you add up all of the results of the multiplications?

def scanning(corupted_memory):
    return re.findall(r"(?:mul\()\d{1,3}[,]\d{1,3}(?:\))", corupted_memory)

def sum_multiplications(list_of_pairs):
    sum = 0
    for pair in list_of_pairs:
        # removing braces and changing data type from string to integer
        a,b = [int(e) for e in pair.lstrip('mul(').rstrip(')').split(',')]
        sum += a*b
    return sum
# scanning uncorrupted multiplications
scanned = []
scanned = scanning(corupted_memory)
adding_multiplications = sum_multiplications(scanned)
print(adding_multiplications)

# Part 2
# example
# corupted_memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

# find do() and don't() in string, split to list and take only parts starting with do()
do_positions = [i for i in range(len(corupted_memory)) if corupted_memory.startswith('do()', i)]
dont_positions = [i for i in range(len(corupted_memory)) if corupted_memory.startswith('don\'t()', i)]
do_positions.append(0) # by default we consider enabled from start    
do_positions.sort()

# we split string corupted_memory and take all substrings starting with 'do()' 
add_mul = 0
for i, index_of_start in enumerate(do_positions):
    # list of possible end-indices for substring (endind with "don't")
    list_of_end_index = [index for index in dont_positions if index_of_start <= index]
    # or substring can end by next 'do()'
    if i < (len(do_positions)-1): 
        list_of_end_index.append(do_positions[i+1])
    else:
        # if there is no more 'do()', then consider end of original string
        list_of_end_index.append(len(corupted_memory)-1)
    # final end-index of substring
    index_of_end = min(list_of_end_index)
    # and do what we 
    add_mul += sum_multiplications(scanning(corupted_memory[index_of_start:index_of_end]))
print(scanned)
print(add_mul)
