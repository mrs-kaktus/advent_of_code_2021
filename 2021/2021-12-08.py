# signals = [
#     'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
#     'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
#     'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
#     'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
#     'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
#     'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
#     'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
#     'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
#     'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
#     'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
#     ]

# four_digit_output = []
# four_digit_output_length = []
# for signal in signals:
#     list_of_strings = signal.split(' | ')[1].split(' ')
#     four_digit_output += list_of_strings
#     # four_digit_output.append(list_of_strings)
#     four_digit_output_length += [len(string) for string in list_of_strings]
#     # four_digit_output_length.append([len(string) for string in list_of_strings])

# four_digit_output = []
# four_digit_output_length = []
# with open('seven_segment_search.txt', 'r') as f:
#     for line in f:
#         list_of_strings = line.rstrip().split(' | ')[1].split(' ')
#         four_digit_output += list_of_strings
#         four_digit_output_length += [len(string) for string in list_of_strings]
#
# print(four_digit_output)
# print(four_digit_output_length)
# print(four_digit_output_length.count(2) + four_digit_output_length.count(3) + four_digit_output_length.count(4) + four_digit_output_length.count(7))

# part two
four_digit_output = []
all_digit_output = []
with open('2021/additional_files/seven_segment_search.txt', 'r') as f:
    for line in f:
        list_of_strings = line.split(' | ')[0].split(' ')
        list_of_strings_four_digit = line.rstrip().split(' | ')[1].split(' ')
        # four_digit_output += list_of_strings
        four_digit_output.append(["".join(sorted(s)) for s in list_of_strings_four_digit])
        all_digit_output.append(["".join(sorted(s)) for s in list_of_strings])


# for line in signals:
#     list_of_strings = line.split(' | ')[0].split(' ')
#     list_of_strings_four_digit = line.rstrip().split(' | ')[1].split(' ')
#     # four_digit_output += list_of_strings
#     four_digit_output.append(["".join(sorted(s)) for s in list_of_strings_four_digit])
#     all_digit_output.append(["".join(sorted(s)) for s in list_of_strings])
# print(four_digit_output)
# print(len(four_digit_output))
# print(all_digit_output)
# print(len(all_digit_output))

def mapping_function(strings):
    # rules:
    #         if length=2 then number 1;
    #         if length=3 then number 7;
    #         if length=4 then number 4;
    #         if length=7 then number 8
    #         if length=6 and values of 4 included then number 9
    #         if length=6 and values of 7 included a nd number 9 dedicated then number 0
    #         if length=6 and number 6 and 9 dedicated then number 6
    #         if length=5 and values of 7 included then number 3
    #         if length=5 and length of intersect of {values of 4} and {values of actual} = 3 then number 5
    #         if length=5 and number 3 and 5 dedicated then number 2
    digits = {digit: "" for digit in range(10)}
    while any([value == '' for value in digits.values()]):
        for s in strings:
            if len(s) == 2:
                digits[1] = s
            elif len(s) == 3:
                digits[7] = s
            elif len(s) == 4:
                digits[4] = s
            elif len(s) == 7:
                digits[8] = s
            elif len(s) == 6 and set(digits[4]).intersection(set(s)) == set(digits[4]):
                digits[9] = s
            elif len(s) == 6 and set(digits[7]).intersection(set(s)) == set(digits[7]) and len(digits[9]) > 0:
                digits[0] = s
            elif len(s) == 6 and len(digits[0]) > 0 and len(digits[9]) > 0:
                digits[6] = s
            elif len(s) == 5 and set(digits[7]).intersection(set(s)) == set(digits[7]) and len(set(digits[4]).intersection(set(s))) == 3:
                digits[3] = s
            elif len(s) == 5 and len(set(digits[4]).intersection(set(s))) == 3 and len(digits[3]) > 0:
                digits[5] = s
            elif len(s) == 5 and len(digits[3]) > 0 and len(digits[5]) > 0:
                digits[2] = s
            # print(s)
    return digits

def decode_digit(decoding_dict, input_list):
    decoded_list = []
    for e in input_list:
        for key in decoding_dict:
            if e == decoding_dict[key]:
                decoded_list.append(key)
    return decoded_list

list_of_decoded_four_digits = []
for index in range(len(all_digit_output)):
    decoded_list = []
    digits = mapping_function(all_digit_output[index])
    numbers = decode_digit(digits, four_digit_output[index])
    list_of_decoded_four_digits.append(int(''.join([str(e) for e in numbers])))
    digits = {digit: "" for digit in range(10)}

print(f'Output: {sum(list_of_decoded_four_digits)}')



