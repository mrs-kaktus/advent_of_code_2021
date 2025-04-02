# part one
# input = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
# ]

str_input = []
with open('2021/additional_files/diagnostic.txt', 'r') as f:
    for line in f:
        str_input.append(str(line.rstrip()))
print(str_input)


def list_of_str_to_int(list_of_str):
    list_of_int = []
    for index, value in enumerate(list_of_str):
        # input[index] = [int(x) for x in list(value)] # this works for example
        list_of_int.append([int(x) for x in list(value)])
    return list_of_int

def transpose(input_matrix):
    return [list(row) for row in zip(*input_matrix)]

def find_most_least_bits_in_row(input_list, equal_count_take_1=True):
    # print(row, len(row), sum(row))
    if sum(input_list) > len(input_list)/2:
        most_bits = 1
        least_bits = 0
    elif sum(input_list) < len(input_list)/2:
        most_bits = 0
        least_bits = 1
    else:
        if equal_count_take_1:
            most_bits = 1
            least_bits = 0
        else:
            most_bits = 0
            least_bits = 1
    return most_bits, least_bits

def find_most_least_bits_in_array(input_array):
    most_bits_list = []
    least_bits_list = []
    for row in input_array:
        most_bits_list.append(find_most_least_bits_in_row(row)[0])
        least_bits_list.append(find_most_least_bits_in_row(row)[1])
        # print(row, len(row), sum(row))
        # if sum(row) >= len(row)/2:
        #     most_bits_list.append(1)
        #     least_bits_list.append(0)
        # else:
        #     most_bits_list.append(0)
        #     least_bits_list.append(1)
    return most_bits_list, least_bits_list

# list of strings to list of integers
input = list_of_str_to_int(str_input)

# transpose matrix
# t_input = list(map(list, zip(*input)))
# t_input = [list(row) for row in zip(*input)]
t_input = transpose(input)

gamma_binary, epsilon_binary = find_most_least_bits_in_array(t_input)

# from list to string
gamma_binary = ''.join(str(e) for e in gamma_binary)
epsilon_binary = ''.join(str(e) for e in epsilon_binary)

# from binary to decimal
gamma_rate = int(gamma_binary, 2)
epsilon_rate = int(epsilon_binary, 2)

power_consumption = gamma_rate * epsilon_rate

print(gamma_binary)
print(epsilon_binary)
print("Power consumption:")
print(power_consumption)

# part two
# verify life support rating
# life_support_rating = oxygen_generator_rating * CO2_scrubber_rating
# oxygen_generator_rating
# CO2_scrubber_rating

# oxygen generator rating

exp_str_input = str_input
exp_t_input = t_input
oxygen_indices = []
oxygen_bit_criteria = ""
oxygen_generator_rating_binary = ""
bit_column = 0
while len(exp_str_input) > 1:
    most_bits, least_bits = find_most_least_bits_in_row(exp_t_input[bit_column])
    oxygen_bit_criteria += str(most_bits)
    for index, value in enumerate(exp_str_input):
        if value.startswith(oxygen_bit_criteria):
            oxygen_indices.append(index)
        # elif value.startswith(CO2_bit_criteria):
        #     CO2_indices.append(index)
        else:
            pass
    exp_str_input = [exp_str_input[i] for i in oxygen_indices]
    exp_input = list_of_str_to_int(exp_str_input)
    exp_t_input = transpose(exp_input)
    oxygen_indices = []
    bit_column += 1
    if len(exp_str_input) == 1:
        oxygen_generator_rating_binary  = ''.join(str(e) for e in exp_str_input)


exp_str_input = str_input
exp_t_input = t_input
CO2_indices = []
CO2_bit_criteria = ""
CO2_scrubber_rating_binary = ""
bit_column = 0
while len(exp_str_input) > 1:
    most_bits, least_bits = find_most_least_bits_in_row(exp_t_input[bit_column])
    CO2_bit_criteria += str(least_bits)
    for index, value in enumerate(exp_str_input):
        if value.startswith(CO2_bit_criteria):
            CO2_indices.append(index)
        # elif value.startswith(CO2_bit_criteria):
        #     CO2_indices.append(index)
        else:
            pass
    exp_str_input = [exp_str_input[i] for i in CO2_indices]
    exp_input = list_of_str_to_int(exp_str_input)
    exp_t_input = transpose(exp_input)
    CO2_indices = []
    bit_column += 1
    if len(exp_str_input) == 1:
        CO2_scrubber_rating_binary = ''.join(str(e) for e in exp_str_input)

# from binary to decimal
oxygen_generator_rating = int(oxygen_generator_rating_binary, 2)
CO2_scrubber_rating = int(CO2_scrubber_rating_binary, 2)
life_support_rating = oxygen_generator_rating * CO2_scrubber_rating

print('Life support rating:')
print(life_support_rating)
