jury_members = int(input())

total_score = 0
counter_presentations = 0
grades_counter = 0
overall_sum_grades = 0
command = input()
while command != "Finish":
    for i in range(jury_members):
        jury_score = float(input())
        grades_counter += 1
        total_score += jury_score
        overall_sum_grades += jury_score
    total_score /= jury_members
    print(f"{command} - {total_score:.2f}.")
    total_score = 0
    jury_score = 0
    command = input()
average_grades = overall_sum_grades / grades_counter
print(f"Student's final assessment is {average_grades:.2f}.")
