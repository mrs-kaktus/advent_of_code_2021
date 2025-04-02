import numpy as np

# input = [
#     '0,9 -> 5,9',
#     '8,0 -> 0,8',
#     '9,4 -> 3,4',
#     '2,2 -> 2,1',
#     '7,0 -> 7,4',
#     '6,4 -> 2,0',
#     '0,9 -> 2,9',
#     '3,4 -> 1,4',
#     '0,0 -> 8,8',
#     '5,5 -> 8,2'
# ]

def is_equal_in_axis(row,axe = 'x'):
    point_1 = [int(e) for e in row.split(' -> ')[0].split(',')]
    point_2 = [int(e) for e in row.split(' -> ')[1].split(',')]
    if axe == 'x':
        is_equal = point_1[0] == point_2[0]
    elif axe == 'y':
        is_equal = point_1[1] == point_2[1]
    return is_equal

def transform_to_line_coordinates(row):
    point_1 = [int(e) for e in row.split(' -> ')[0].split(',')]
    point_2 = [int(e) for e in row.split(' -> ')[1].split(',')]
    # horizontal and verical lines
    if is_equal_in_axis(row, 'x'):
        y_start_end = sorted([point_1[1], point_2[1]])
        y_coords = range(y_start_end[0], y_start_end[1] + 1)
        x_coords = [point_1[0]] * len(y_coords)
    elif is_equal_in_axis(row, 'y'):
        x_start_end = sorted([point_1[0], point_2[0]])
        x_coords = range(x_start_end[0], x_start_end[1] + 1)
        y_coords = [point_1[1]] * len(x_coords)
    # diagonal lines
    else:
        if point_1[1] > point_2[1]:
            y_start_end = sorted([point_1[1], point_2[1]])
            y_coords = list(range(y_start_end[0], y_start_end[1] + 1))
            y_coords.reverse()
        else:
            y_start_end = [point_1[1], point_2[1]]
            y_coords = list(range(y_start_end[0], y_start_end[1] + 1))
        if point_1[0] > point_2[0]:
            x_start_end = sorted([point_1[0], point_2[0]])
            x_coords = list(range(x_start_end[0], x_start_end[1] + 1))
            x_coords.reverse()
        else:
            x_start_end = [point_1[0], point_2[0]]
            x_coords = list(range(x_start_end[0], x_start_end[1] + 1))
    return np.array([[x, y] for x, y in zip(x_coords, y_coords)])

def write_line_into_diagram(input_coords, input_diagram = np.zeros((10, 10)), length_of_diagram = 10):
    diagram_with_line = np.zeros((length_of_diagram, length_of_diagram))
    diagram_with_line[input_coords[:, 1], input_coords[:, 0]] = 1
    input_diagram += diagram_with_line
    return input_diagram

def count_points_of_overlap(input_diagram):
        return (diagram >= 2).sum()


input = []
with open('additional_files/hydrothermal_vents_lines.txt', 'r') as f:
    for row in f:
        input.append(row.rstrip())
print(input)

# diagram = np.zeros((10, 10)) #for example
diagram = np.zeros((1000, 1000))
for line in input:
    # part one:
    # if is_equal_in_axis(line, 'x') or is_equal_in_axis(line, 'y'):
    #     coords = transform_to_line_coordinates(line)
    #     diagram = write_line_into_diagram(coords, diagram, 1000)
    # else:
    #     pass
    
    # part two:
    coords = transform_to_line_coordinates(line)
    diagram = write_line_into_diagram(coords, diagram, 1000)

points_of_overlap = count_points_of_overlap(diagram)
print('Points of overlap:')
print(points_of_overlap)

# part two - diagonal lines and points of overlapping