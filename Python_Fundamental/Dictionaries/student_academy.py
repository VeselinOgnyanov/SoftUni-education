pair_of_rows = int(input())
students_dict = {}
final_dict = {}
for number_of_row in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(student_grade)

for key, value in students_dict.items():
    iterable = value
    result = sum(iterable) / len(value)
    if result >= 4.50:
        final_dict[key] = result

for final_key, final_value in final_dict.items():
    print(f"{final_key} -> {final_value:.2f}")
