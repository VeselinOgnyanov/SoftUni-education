name = input()

counter_grades = 1
counter_poor_grades = 0
average_grade = 0
expelled = False
while counter_grades <= 12:
    grade = float(input())
    if grade >= 4:
        counter_grades += 1
        counter_poor_grades = 0
        average_grade += grade
    else:
        counter_poor_grades += 1
    if counter_poor_grades > 1:
        expelled = True
        break
average_grade /= 12
if expelled:
    print(f"{name} has been excluded at {counter_grades} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
