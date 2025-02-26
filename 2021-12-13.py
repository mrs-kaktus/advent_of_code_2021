import numpy as np
# dots = [
#     [6,10],
#     [0,14],
#     [9,10],
#     [0,3],
#     [10,4],
#     [4,11],
#     [6,0],
#     [6,12],
#     [4,1],
#     [0,13],
#     [10,12],
#     [3,4],
#     [3,0],
#     [8,4],
#     [1,10],
#     [2,14],
#     [8,10],
#     [9,0]
# ]
# folding = ['y=7', 'x=5']
# fold along y=7
# fold along x=5

dots = []
folding = []
with open('additional_files/transparent_paper.txt', 'r') as f:
    for line in f:
        if 'fold along' in line:
            folding.append(line.rstrip().split('fold along ')[1].split('='))
        elif not line.strip():
            continue
        else:
            dots.append([int(float(e)) for e in line.rstrip().split(',')])
# print(dots)
# print(folding)



def fold_along(input_array, axis, fold_on_line):
    # fold_on_line = int(fold_on_line)
    len_x, len_y = input_array.shape
    if axis == 'y':
        upper = input_array[0:fold_on_line, :]
        lower = input_array[list(reversed(range((fold_on_line+1), len_x))), :]
        return upper + lower
    elif axis == 'x':
        left = input_array[:, 0:fold_on_line]
        right = input_array[:, list(reversed(range((fold_on_line+1), len_y)))]
        return left + right

dots_array = np.array(dots)
len_y, len_x = np.amax(dots_array, axis=0) # get lengths of x and y axis
array_with_dots = np.zeros([(len_x+1), (len_y+1)], dtype=bool) # prepare array with zeros
array_with_dots[dots_array[:, 1], dots_array[:, 0]] = True # add dots to array on indices
print(array_with_dots)
print(array_with_dots.shape)


# fold_y = fold_along(array_with_dots, axis = 'y', fold_on_line=7)
# print("function fold_along: y=7")
# print( fold_y.astype(int))
# print(fold_y.sum())
#
# fold_x = fold_along(fold_y, axis = 'x', fold_on_line=5)
# print("function fold_along: x=5")
# print(fold_x.astype(int))
# print(fold_x.astype(int).sum())

# part one
fold_x = fold_along(array_with_dots, axis='x', fold_on_line=655)
print("function fold_along: x=5")
print(fold_x.astype(int))

print(fold_x.sum())

# part two
folded_paper = array_with_dots
for fold in folding:
    folded_paper = fold_along(folded_paper, axis=fold[0], fold_on_line=int(fold[1]))

folded_paper_string = np.zeros(folded_paper.shape)
folded_paper_string = np.where(folded_paper == True, '#', folded_paper_string)
folded_paper_string = np.where(folded_paper == False, '.', folded_paper_string)
print('Foldied the transparent paper:')
for l in folded_paper_string:
    print(''.join(l))

