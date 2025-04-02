import numpy as np


def neighbors_pixels(a, row_index, column_index, radius=1):
    neighbours_array = []
    for i in range(row_index - radius, row_index + 1 + radius):
        for j in range(column_index - radius, column_index + 1 + radius):
            if 0 <= i < (len(a)) and 0 <= j < len(a[0]):
                neighbours_array.append(a[i][j])
            else:
                pass
                # neighbours_array.append('.')
    return neighbours_array


def extend_image(image_array, extending_symbol='.', extend_radius=5):
    image_array_np = np.array(image_array)
    # add rows
    row_to_append = np.array([[extending_symbol] * image_array_np.shape[1]] * extend_radius)
    extended_array_upper_rows = np.append(row_to_append, image_array, 0)
    extended_array_upper_and_lower_rows = np.append(extended_array_upper_rows, row_to_append, 0)
    # add columns
    columns_to_append = np.array([[extending_symbol] * extend_radius] * extended_array_upper_and_lower_rows.shape[0])
    extended_array_left_columns = np.append(columns_to_append, extended_array_upper_and_lower_rows, 1)
    extended_array_left_and_right_columns = np.append(extended_array_left_columns, columns_to_append, 1)
    return extended_array_left_and_right_columns.tolist()


def extend_if_needed(image_array):
    image_array_np = np.array(image_array)
    if len(np.unique(image_array_np[:3, :])) == 2 or len(np.unique(image_array_np[-3:, :])) == 2 or len(np.unique(image_array_np[:, :3])) == 2 or len(np.unique(image_array_np[:, -3:])) == 2:
        result = extend_image(image_array, extending_symbol=image_array_np[0, 0], extend_radius=5)
    else:
        result = image_array
    return result


def apply_algorithm_to_every_pixel(image_array, image_enhancement_algorithm):
    updated_image = []
    updated_row = []
    for row in range(len(image_array)):
        for column in range(len(image_array[0])):
            # pixels_in_bin = ''.join(neighbors_pixels(image_array, row, column))
            pixels_in_bin = ''.join(neighbors_pixels(image_array, row, column))
            index_in_algorithm = int(pixels_in_bin.replace('.', '0').replace('#', '1'), 2)
            updated_row.append(image_enhancement_algorithm[index_in_algorithm])
        updated_image.append(updated_row)
        updated_row = []
    return updated_image

#
# image_enhancement_algorithm = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
#
# image = [
#     '#..#.',
#     '#....',
#     '##..#',
#     '..#..',
#     '..###'
# ]

# INPUT
image = []
with open('2021/additional_files/trench_map.txt', 'r') as f:
    image_enhancement_algorithm = f.readline()
    f.readline()
    for line in f:
        image.append(line.rstrip())
print(f'image_enhancement_algorithm: {image_enhancement_algorithm}')
print(f'image: {image}')


# formating image from list of strings to array of strings
image_array = [list(e) for e in image]

print('Original image: ')
extended_image_array = extend_image(image_array)
for row in extended_image_array:
    print(''.join(row))

# apply algorithm
applied_image_array = extended_image_array
for i in range(50):
    print(f'Applied no.: {i + 1}')
    image_array_np = np.array(applied_image_array)
    extended_image_array = extend_if_needed(applied_image_array)
    applied_image_array = apply_algorithm_to_every_pixel(extended_image_array, image_enhancement_algorithm)
    print('Result: ')
    for row in applied_image_array:
        print(''.join(row))

count_lit_pixels = np.count_nonzero(np.array(applied_image_array) == '#')
print(f'Number of lit pixels: {count_lit_pixels}')
# part one
# after 2 applies
# 4964 #ok

# part two
# after 50 applies
# 187176 #nope
# 18847 #nope too high
# 12817 # nope loo low
# 13202 # yep