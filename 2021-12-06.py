# initial = [3,4,3,1,2]
# print(initial)

with open('additional_files/lanternfish.txt', 'r') as f:
    initial = [int(e) for e in f.readline().rstrip().split(',')]
print(initial)

def count_states_for_next_days(input_states, days = 1):
    actual_states = input_states
    for day in range(days):
        new_states = {state: 0 for state in range(9)}
        # actual state <> 0
        for state in range(8):
            new_states[state] = actual_states[state + 1]
        # actual state 0
        new_states[6] += actual_states[0]
        new_states[8] = actual_states[0]
        actual_states = new_states
    return actual_states

def count_fishes(input_states):
    return sum(input_states.values())

# prepare states and counts from initial
states = {state: 0 for state in range(9)}
for state in states:
    states[state] = initial.count(state)

new_states = count_states_for_next_days(states, 80)
total_fishes = count_fishes(new_states)
print('Total fishes after 80 days:')
print(total_fishes)


# part two
# after 256 days
new_states = count_states_for_next_days(states, 256)
total_fishes = count_fishes(new_states)
print('Total fishes after 256 days:')
print(total_fishes)
