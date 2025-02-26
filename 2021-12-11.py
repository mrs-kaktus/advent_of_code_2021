import numpy as np
# input = [
#     '5483143223',
#     '2745854711',
#     '5264556173',
#     '6141336146',
#     '6357385478',
#     '4167524645',
#     '2176841721',
#     '6882881134',
#     '4846848554',
#     '5283751526'
# ]
# energy_level = []
# for row in input:
#     energy_level.append([int(e) for e in list(row)])
# energy_level = np.array(energy_level)
# print(energy_level)

energy_level = []
with open('starting_energy_levels.txt', 'r') as f:
    for line in f:
        energy_level.append([int(e) for e in list(line.rstrip())])
energy_level = np.array(energy_level)
print(energy_level)

def increase_energy_by_one(input_array):
    input_array += np.ones(input_array.shape, dtype=int)
    return input_array

def increase_for_neighbours(pos, matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    matrix_with_neighbours = np.zeros(matrix.shape, dtype=int)
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            if [i, j] != pos:
                matrix_with_neighbours[i][j] += 1
    return matrix_with_neighbours

def check_grid_and_flash(input_array):
    # increase energy adjacent octopus
    new_positions = np.argwhere(input_array >= 9).tolist()
    positions = []
    while len(new_positions) > 0:
        positions.extend(new_positions)
        for indices in new_positions:
            input_array += increase_for_neighbours(indices, input_array)
        new_positions = np.argwhere(input_array >= 9).tolist()
        new_positions = [item for item in new_positions if item not in positions] # what is in new position but not in positions
        # increase only new indices, that had just come to >=9 in this loop

    # after flashed decreased energy to 0
    input_array = np.where(input_array >= 9, -1, input_array)
    return input_array


# moment_all_flas = []
total_flashes = 0
for i in range(100):
    print('step')
    print(i+1)
    print('increase')
    energy_level = increase_energy_by_one(energy_level)
    print(energy_level)
    # total_flashes += np.count_nonzero(energy_level == 0)
    # if np.count_nonzero(energy_level == 0) == (energy_level.shape[0] * energy_level.shape[1]):  # all flash
    #     moment_all_flas.append(i + 1)
    print(total_flashes)
    energy_level = check_grid_and_flash(energy_level)

# part two (1. version)
# print('First moment when all flash')
# print(min(moment_all_flas))

# part two (2. version)
i = 0
while np.count_nonzero(energy_level == 0) != (energy_level.shape[0] * energy_level.shape[1]):  # all flash
    print('step')
    print(i+1)
    # print(total_flashes)
    energy_level = check_grid_and_flash(energy_level)
    energy_level = increase_energy_by_one(energy_level)
    print(energy_level)
    i +=1



