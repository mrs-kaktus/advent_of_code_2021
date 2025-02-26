import numpy as np
# part one

# numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# boards = [
#     np.array([
#         [22, 13, 17, 11,  0],
#         [8 , 2, 23,  4, 24],
#         [21,  9, 14, 16,  7],
#         [6 ,10,  3, 18,  5],
#         [1, 12, 20, 15, 19]
#     ]),
#     np.array([
#         [3, 15,  0,  2, 22],
#         [9, 18, 13, 17,  5],
#         [19,  8,  7, 25, 23],
#         [20, 11, 10, 24,  4],
#         [14, 21, 16, 12,  6]
#     ]),
#     np.array([
#         [14, 21, 17, 24,  4],
#         [10, 16, 15,  9, 19],
#         [18,  8, 23, 26, 20],
#         [22, 11, 13,  6,  5],
#         [2,  0, 12,  3,  7]
#     ])
# ]
#

# board = np.array([[14, 21, 17, 24,  4],
#         [10, 16, 15,  9, 19],
#         [18,  8, 23, 26, 20],
#         [22, 11, 13,  6,  5],
#         [2,  0, 12,  3,  7]
#                   ])

boards = []  # hold matrixA, matrixB, ...
board = []  # hold current matrix
with open('bingo_boards.txt', 'r') as f:
    numbers = [int(e) for e in f.readline().rstrip().split(",")]
    f.readline()
    for line in f:
        # values = line.split()
        values = [int(e) for e in line.split()]
        if values:  # if line contains numbers
            board.append(values)
        else:  # if line contains nothing then add board to boards
            boards.append(np.array(board))
            board = []

def transpose(input_matrix):
    return [list(row) for row in zip(*input_matrix)]

def mark_index_of_drawn_number(drawn_number, input_array, input_array_with_indices):
    return np.logical_or(input_array == drawn_number, input_array_with_indices)

def check_completed_row_column(input_array):
    is_completed_row = any([sum(row) == len(row) for row in input_array])
    is_completed_column = any([sum(column) == len(column) for column in transpose(input_array)])
    return is_completed_row or is_completed_column

def count_steps_to_win_and_marked_indices(input_numbers, input_array, input_array_of_indices = np.tile(False, (5, 5))):
    index = 0 # as index of list input_numbers and also as counter of steps to win
    while not(check_completed_row_column(input_array_of_indices)):
        input_array_of_indices = mark_index_of_drawn_number(input_numbers[index], input_array, input_array_of_indices)
        index += 1
    return index - 1, input_array_of_indices

def sum_of_all_unmarked_numbers(input_array, input_array_of_indices):
    indices = np.bitwise_not(input_array_of_indices) # take unmarked indices
    return np.sum(input_array[indices])

def final_score(input_numbers, input_array):
    number_index, marked_indices = count_steps_to_win_and_marked_indices(input_numbers, input_array)
    return sum_of_all_unmarked_numbers(input_array, marked_indices) * numbers[number_index], number_index

board_scores = []
boards_steps_to_win = []
for board in boards:
    score, steps_to_win = final_score(numbers, board)
    board_scores.append(score)
    boards_steps_to_win.append(steps_to_win)

index_min = np.argmin(boards_steps_to_win) # index of first winning board
score_of_winning_board = board_scores[index_min]

print('Final score:')
print(score_of_winning_board)

# part two
#last winning board
index_max = np.argmax(boards_steps_to_win) # index of first winning board
score_of_last_winning_board = board_scores[index_max]
print('Final score of last winning board:')
print(score_of_last_winning_board)
