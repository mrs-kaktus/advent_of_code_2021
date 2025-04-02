# Player 1 starting position: 4
# Player 2 starting position: 8

#INPUT
# Player 1 starting position: 7
# Player 2 starting position: 2

def roll_dice(dice_state):
    # return sum of 3 times rolled dice and new state of dice
    return sum(range(dice_state, dice_state + 3)), dice_state + 3

def turn(position, score, dice_state):
    forward_steps, new_dice_state = roll_dice(dice_state)
    new_position = ((position + forward_steps-1) % 10)+1
    new_score = score + new_position
    return new_position, new_score, new_dice_state

def check_score(score_one, score_two, limit = 1000):
    if score_one >= limit:
        is_winner = True
        winner = 'player_one'
    elif score_two >= limit:
        is_winner = True
        winner = 'player_two'
    else:
        is_winner = False
        winner = 'nobody'
    return is_winner, winner

dice_state = 1

player_one_score = 0
player_two_score = 0

player_one_position = 7
player_two_position = 2

is_winner = False
winner = ''
round_no = 0
dice_rolls = 0
while not(is_winner):
    round_no += 1
    # player one's turn
    player_one_position, player_one_score, dice_state = turn(player_one_position, player_one_score, dice_state)
    dice_rolls += 3
    # check if player_one is winner
    is_winner, winner = check_score(player_one_score, player_two_score)
    # player two's turn
    if winner != 'player_one':
        player_two_position, player_two_score, dice_state = turn(player_two_position, player_two_score, dice_state)
        dice_rolls += 3
        # check score
        is_winner, winner = check_score(player_one_score, player_two_score)
    else:
        break
print(f'Final round no: {round_no}')
print(f'player_one_position: {player_one_position}')
print(f'player_one_score: {player_one_score}')
print(f'player_two_position: {player_two_position}')
print(f'player_two_score: {player_two_score}')
print(f'dice_state: {dice_state}')
print(f'dice_rolls: {dice_rolls}')

result = player_two_score * dice_rolls
print(f'Result: {result}')


# part two


def turn_ii(position, score, round_no=0):
    round_no += 1
    forward_steps = list(range(3, 10))
    new_positions = [((position + forward_step - 1) % 10) + 1 for forward_step in forward_steps]
    new_scores = [score + new_position for new_position in new_positions]
    for new_score, new_position in zip(new_scores,new_positions):
        if new_score < 21:
            turn_ii(score, new_position)
        else:
            pass
    return new_positions, new_scores, round_no