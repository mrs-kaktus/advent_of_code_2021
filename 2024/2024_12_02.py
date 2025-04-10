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
        # print([int(e) for e in line.split()])
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
    if len(unique_report_values) != len(report): # contains dupllicites - cannot be trully sorted
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
# The same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
# We can just adjust functions

def adj_is_report_safe(report):
    if is_report_safe(report) == True:
        return True
    elif cond_adjacent_levels(report) == False:
        # Any two adjacent levels differ by at least one and at most three.
        # with adjustment if one level is removed, report would fulfill condition of safety    
        indices = []
        for i,e in enumerate(report):
            if i > 0 and i < (len(report)-1) and (abs(e - report[i+1]) > 3 or abs(report[i-1] - e) > 3):
               indices.append(i)
            elif i == 0 and abs(e - report[i+1]) > 3:
                indices.append(i)
            elif i == (len(report)-1) and abs(report[i-1] - e) > 3:
                indices.append(i)
        # check all candidates for removing and run original function cond_adjacent_levels()
        for i in indices:
            if is_report_safe(report[:i] + report[i+1:]) == True:
                return True
        return False
    elif cond_increase_or_decrease(report) == False:
        # The levels are either all increasing or all decreasing.
        # with adjustment if there is just one duplicity, could be removed and report will fulfill condition of safety
        unique_report_values = list(set(report))
        if len(unique_report_values) < (len(report)-1): # if it contains more duplicities, removing one level can not hep, so it is unsafe 
            return False
        elif len(unique_report_values) == (len(report)-1): # if it contains just one duplicity, can be removed and be incersing/decreasing
            [first_index, second_index] = [i for i, e in enumerate(report) if report.count(e) > 1]
            if is_report_safe(report[:first_index] + report[(first_index+1):]):
                return  True
            elif is_report_safe(report[:second_index] + report[(second_index+1):]):
                return True
        # disturbing level(s)
        sorted_report = sorted(report)
        reversed_sorted_report = sorted(report,reverse=True)

        if report != sorted_report:
            disturbing_levels = [i for i, e in enumerate(report) if report[i]!= sorted_report[i]]
        elif report != reversed_sorted_report:
            disturbing_levels = [i for i, e in enumerate(report) if report[i]!= reversed_sorted_report[i]]
        for i in disturbing_levels:
            if is_report_safe(report[:i] + report[i+1:]) == True:
                return True
    else:
        return False

counter = 0
for r in reports:
    if adj_is_report_safe(r):
            counter +=1
print(f'Number of safe reports (after adjustment): {counter}')
