# template = 'NNCB'
# rules = [
# 'CH -> B',
# 'HH -> N',
# 'CB -> H',
# 'NH -> C',
# 'HB -> C',
# 'HC -> B',
# 'HN -> C',
# 'NN -> C',
# 'BH -> H',
# 'NC -> B',
# 'NB -> B',
# 'BN -> B',
# 'BB -> N',
# 'BC -> B',
# 'CC -> N',
# 'CN -> C'
# ]

def polymerization_step(template, rules_dict):
    new_polymer = template[0]
    for index in range(len(template)-1):
        key = template[index] + template[index + 1]
        new_polymer += rules_dict[key] + template[index + 1]
    return new_polymer

rules = []
with open('polymer_template_and_pair_rules.txt', 'r') as f:
    template = f.readline().rstrip()
    f.readline()
    for line in f:
        rules.append(line.rstrip())
print(template)
print(rules)

rules_dict = {}
for e in rules:
    rules_dict[e.split(' -> ')[0]] = e.split(' -> ')[1]

new_polymer = template[:]
for step in range(10):
    new_polymer = polymerization_step(new_polymer, rules_dict)
    # print(new_polymer)
print('final new_polymer')
print(new_polymer)


unique_characters = ''.join(set(new_polymer))
print()

character_count = []
for e in list(unique_characters):
    print(f'Occurencec of {e}:')
    print(new_polymer.count(e))
    character_count.append(new_polymer.count(e))

print('Difference between MAX and MIN:')
print(max(character_count) - min(character_count))
# 2509

# part two

def polymerization_step_counter(counter_dict, last_pair, rules_dict):
    updated_counter = dict.fromkeys(counter_dict.keys(), 0)
    for key in counter_dict.keys():
        updated_counter[rules_dict[key] + key[1]] += counter_dict[key] # right part of new polymer
        updated_counter[key[0] + rules_dict[key]] += counter_dict[key] # left part of new polymer
        if key == last_pair:
            updated_last_pair = rules_dict[key] + key[1]
    return updated_counter, updated_last_pair


rules = []
with open('polymer_template_and_pair_rules.txt', 'r') as f:
    template = f.readline().rstrip()
    f.readline()
    for line in f:
        rules.append(line.rstrip())
print(f'template: {template}')
print(f'rules: {rules}')

rules_dict = {}
for e in rules:
    rules_dict[e.split(' -> ')[0]] = e.split(' -> ')[1]


counter_dict = dict.fromkeys(rules_dict.keys(), 0)
last_pair = template[-2:]
#set counter on initial template
for index in range(len(template)-1):
    key = template[index] + template[index + 1]
    counter_dict[key] += 1
print('count of initial template:')
print(counter_dict)


# steps of polymerization
for i in range(40):
    counter_dict, last_pair = polymerization_step_counter(counter_dict, last_pair, rules_dict)
print(f'final counts:{counter_dict}')


unique_characters = list(set([item for sublist in rules_dict.keys() for item in sublist]))
print(f'unique_characters :{unique_characters}')
final_counter = dict.fromkeys(unique_characters, 0)
for key in counter_dict:
    final_counter[key[0]] += counter_dict[key]
    if key == last_pair:
        final_counter[key[1]] += 1
print(f'final_counter: {final_counter}')

print('Difference between MAX and MIN:')
print(max(final_counter.values()) - min(final_counter.values()))
