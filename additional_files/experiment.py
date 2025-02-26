
def is_equal_in_axis(row,axe = 'x'):
    point_1 = [int(e) for e in row.split(' -> ')[0].split(',')]
    point_2 = [int(e) for e in row.split(' -> ')[1].split(',')]
    if axe == 'x':
        is_equal = point_1[0] == point_2[0]
    elif axe == 'y':
        is_equal = point_1[1] == point_2[1]
    return is_equal

row = '9,4 -> 3,4'
point_1 = [int(e) for e in row.split(' -> ')[0].split(',')]
point_2 = [int(e) for e in row.split(' -> ')[1].split(',')]
if is_equal_in_axis(row, 'x'):
    y_start_end = sorted([point_1[1], point_2[1]])
    y_coords = range(y_start_end[0], y_start_end[1] + 1)
    x_coords = [point_1[0]] * len(y_coords)
elif is_equal_in_axis(row, 'y'):
    x_start_end = sorted([point_1[0], point_2[0]])
    x_coords = range(x_start_end[0], x_start_end[1] + 1)
    y_coords = [point_1[1]] * len(x_coords)
print([[x, y] for x, y in zip(x_coords, y_coords)])

