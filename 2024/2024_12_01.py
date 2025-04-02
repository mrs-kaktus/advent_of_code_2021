#  Part 1
# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
# left_list = [3,4,2,1,3,3]
# right_list = [4,3,5,3,9,3]
left_list = []
right_list = []
with open("2024/additional_files/lists_of_locations.txt", "r") as f:
    for line in f:
        # print(int(line.rstrip().split()[0]))
        # print(int(line.rstrip().split()[1]))
        left_list.append(int(line.rstrip().split()[0]))
        right_list.append(int(line.rstrip().split()[1]))

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

# #how far apart the two numbers are; you'll need to add up all of those distances#
dist = []
for i in range(len(sorted_left_list)):
    dist.append(abs(sorted_right_list[i]-sorted_left_list[i]))

# total distance
print(f'total distance: {sum(dist)}')

# Part 2
# how often each number from the left list appears in the right list
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

unique_left_list = list(set(left_list))
similarity_score= dict((i, right_list.count(i)) for i in unique_left_list)

similarity_score_list = [e*similarity_score[e] for e in left_list]
# sum(similarity_score_list)
# print(similarity_score_list)
print(f'total similarity score: {sum(similarity_score_list)}')
