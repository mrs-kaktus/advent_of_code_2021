# crabs =[16,1,2,0,4,2,7,1,2,14]

with open('2021/additional_files/the_horizontal_position_of_each_crab.txt', 'r') as f:
    crabs = [int(e) for e in f.readline().rstrip().split(',')]
print(crabs)

def find_cheapest_fuel_costs(crabs):
    costs = []
    positions = list(range(1, max(crabs)))
    for position in positions:
        costs.append(sum([abs(position - crab) for crab in crabs]))
    min_cost = min(costs)
    min_index = costs.index(min_cost)
    return min_cost, positions[min_index]

cheapest_fuel_costs, position = find_cheapest_fuel_costs(crabs)
print(f'The Cheapest Fuel Costs: {cheapest_fuel_costs}')

print(f'Position: {position}')

# part two
def fuel_costs_adjusted(position, crab):
    # eg. position = 1, crab = 5, diff = 4, costs= 1+2+3+4
    return sum(list(range(1, abs(position - crab) + 1)))

def find_cheapest_fuel_costs_adjusted(crabs):
    costs = []
    positions = list(range(1, max(crabs)))
    for position in positions:
        costs.append(sum([fuel_costs_adjusted(position, crab) for crab in crabs]))
    min_cost = min(costs)
    min_index = costs.index(min_cost)
    return min_cost, positions[min_index]


cheapest_fuel_costs_adjusted, position = find_cheapest_fuel_costs_adjusted(crabs)
print(f'The Cheapest Fuel Costs: {cheapest_fuel_costs_adjusted}')
print(f'Position: {position}')



