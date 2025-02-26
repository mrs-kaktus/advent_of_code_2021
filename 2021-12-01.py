# part one
# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = []
with open("additional_files/measurements.txt", "r") as f:
    for line in f:
        input.append(int(line.rstrip()))
print(input)

def increase_counter(input_list):
    counter = 0
    for index in range((len(input_list) - 1)):
        if input_list[index] < input_list[index + 1]:
            counter += 1
    print(counter)

print("Number of increased measurements: ")
increase_counter(input)

# part two
three_measurement_window = []
for index in range(1, (len(input) - 1)):
    three_measurement_window.append(input[index - 1] + input[index] + input[index + 1])

print("Number of increased three-measurements window: ")
increase_counter(three_measurement_window)



