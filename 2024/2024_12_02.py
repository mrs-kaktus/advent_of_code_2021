# Part 1

# example
# reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ]
reports = []
with open("2024/additional_files/reports_to_analyze.txt", "r") as f:
    for line in f:
        print([int(e) for e in line.split()])
        reports.append([int(e) for e in line.split()])


# row = report, column = level
# report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


            
def cond_increase_or_decrease(report):
    # The levels are either all increasing or all decreasing.
    sorted_report = sorted(report)
    reversed_sorted_report = sorted(report,reverse=True)
    unique_report_values = list(set(report))
    if len(unique_report_values) != len(report): #contains dupllicites - cannot be trully sorted
        return False 
    elif report == sorted_report or report == reversed_sorted_report:
        return True
    else:
        return False 
    
def cond_adjacent_levels(report):
    # Any two adjacent levels differ by at least one and at most three.
    for i,e in enumerate(report):
        if i > 0 and i < (len(report)-1):
            if abs(e - report[i+1]) > 3 or abs(report[i-1] - e) > 3:
                return False
        elif i == 0:
            if abs(e - report[i+1]) > 3:
                return False
        elif i == (len(report)-1):
            if abs(report[i-1] - e) > 3:
                return False
            else:
                return True
            
def is_report_safe(report):
    return (cond_increase_or_decrease(report) and cond_adjacent_levels(report))

counter = 0
for r in reports:
    if is_report_safe(r):
        counter +=1
print(f'Number of safe reports: {counter}')

# Part 2
