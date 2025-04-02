import numpy as np
#
# input = [
#     '2199943210',
#     '3987894921',
#     '9856789892',
#     '8767896789',
#     '9899965678'
# ]

input = []
with open('2021/additional_files/height_map.txt', 'r') as f:
    for line in f:
        input.append(line.rstrip())
print(input)

def find_neighbours(height_map_array, row, col):
    len_x, len_y = height_map_array.shape
    x = (row, row, row-1, row+1)
    y = (col-1, col+1, col, col)
    return sorted([height_map_array[i[0]][i[1]] for i in zip(x, y) if 0 <= i[0] <= len_x - 1 and 0 <= i[1] <= len_y - 1])

def risk_level(input):
    return sum([i + 1 for i in input])

# preprocessing data
height_map_lists = []
for row in input:
    height_map_lists.append([int(e) for e in row])
height_map_array = np.array(height_map_lists)
print(height_map_array)

# find low poins
low_points = []
low_points_indices = []
for row, values in enumerate(height_map_array):
    for col, point in enumerate(values):
        neighbours = find_neighbours(height_map_array, row, col)
        if point < min(neighbours):
            low_points.append(point)
            low_points_indices.append((row,col))
        else:
            continue

print(f'low_points: {low_points}')
print(f'low_points_indices: {low_points_indices}')
print(f'sum of the risk levels of all low points: {risk_level(low_points)}')


# part two

def find_neighbours_indices(height_map_array, row, col):
    len_x, len_y = np.shape(height_map_array)
    x = (row, row, row-1, row+1)
    y = (col-1, col+1, col, col)
    return sorted([(i[0], i[1]) for i in zip(x, y) if 0 <= i[0] <= len_x - 1 and 0 <= i[1] <= len_y - 1])

def find_basin(height_map_array, row, col, basin_indices):
    neighbours_indices = find_neighbours_indices(height_map_array, row, col)
    for neighbour_index in neighbours_indices:
        if int(height_map_array[row, col]) < height_map_array[neighbour_index] < 9 and (neighbour_index not in basin_indices):
            basin_indices.add(neighbour_index)
            basin_indices.union(find_basin(height_map_array, neighbour_index[0], neighbour_index[1], basin_indices))
        else:
            continue
    return basin_indices

len_basins = []
for low_point_index in low_points_indices:
    basin = find_basin(height_map_array, low_point_index[0], low_point_index[1], {low_point_index})
    len_basins.append(len(basin))
    # print(basin)
    # print(len(basin))
len_basins.sort(reverse=True)
print('Find the three largest basins and multiply their sizes together:')
print(len_basins[0]*len_basins[1]*len_basins[2])


