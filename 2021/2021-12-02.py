# part one
# input = [["forward", 5],
#          ["down", 5],
#          ["forward", 8],
#          ["up", 3],
#          ["down", 8],
#          ["forward", 2]
#          ]

position = {"horizontal": 0, "depth": 0}

input = []
prep_list = []
with open('2021/additional_files/position.txt', 'r') as f:
    for line in f:
        for element in line.rstrip().split():
            prep_list = [line.rstrip().split()[0], int(line.rstrip().split()[1])]
        input.append(prep_list)
print(input)

def move(direction, units, position_dict):
    if direction == "forward":
        position_dict["horizontal"] += units
    elif direction == "down":
        position_dict["depth"] += units
    elif  direction == "up":
        position_dict["depth"] -= units
    return position_dict


for prep_list in input:
    position = move(prep_list[0], prep_list[1], position)

print('Position')
for key in position:
    print(key, position[key])

# part two
position = {"horizontal": 0, "depth": 0, "aim": 0}

def updated_move(direction, units, position_dict):
    if direction == "forward":
        position_dict["horizontal"] += units
        position_dict["depth"] += position_dict["aim"] * units
    elif direction == "down":
        position_dict["aim"] += units
    elif  direction == "up":
        position_dict["aim"] -= units
    return position_dict

for prep_list in input:
    position = updated_move(prep_list[0], prep_list[1], position)

print('Updated calculation - Position:')
for key in position:
    print(key, position[key])