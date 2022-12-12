student_grade_dictionary = {}

number_of_grades = int(input())

for _ in range(number_of_grades):
    name, grade = input().split()
    if name not in student_grade_dictionary.keys():
        student_grade_dictionary[name] = []
    student_grade_dictionary[name].append(grade)

# print(student_grade_dictionary)
# print(len(student_grade_dictionary))
for key, value in student_grade_dictionary.items():
    dictionary_values = list(map(float, value))
    aver = sum(dictionary_values) / len(dictionary_values)
    string_values = " ".join(str(f"{x:.2f}") for x in dictionary_values)
    print(f"{key} -> {string_values} (avg: {aver:.2f})")

