num_poor_grades = int(input())
poor_grades_counter = 0
problem_name = input()
sum_grades = 0
counter_problems = 0
average_sum = 0
much_poor_grades = False
last_name = ()
while problem_name != "Enough":
    grade = int(input())
    if grade <= 4:
        poor_grades_counter += 1
    sum_grades += grade
    counter_problems += 1
    if poor_grades_counter == num_poor_grades:
        much_poor_grades = True
        break
    last_name = problem_name
    problem_name = input()
average_sum = sum_grades / counter_problems
if much_poor_grades:
    print(f"You need a break, {poor_grades_counter} poor grades.")
else:
    print(f"Average score: {average_sum:.2f}")
    print(f"Number of problems: {counter_problems}")
    print(f"Last problem: {last_name}")