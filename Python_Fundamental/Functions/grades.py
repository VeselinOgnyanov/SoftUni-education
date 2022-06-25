def grade(current_grade):
    if (current_grade > 2.00) and (current_grade <= 2.99):
        return "Fail"
    if (current_grade >= 3.00) and (current_grade <= 3.49):
        return "Poor"
    if (current_grade >= 3.50) and (current_grade <= 4.49):
        return "Good"
    if (current_grade >= 4.50) and (current_grade <= 5.49):
        return "Very Good"
    if (current_grade >= 5.50) and (current_grade <= 6.0):
        return "Excellent"


current_grade = float(input())
print(grade(current_grade))
