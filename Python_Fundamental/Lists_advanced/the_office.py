list_of_employee_happiness = list(map(int, (input().split())))
happiness_improvement_factor = int(input())
# print(list_of_employee_happiness)

counter_for_happy_employees = 0

length_of_employees = len(list_of_employee_happiness)
multiplied_happiness = list(map(lambda x: x * happiness_improvement_factor, list_of_employee_happiness))
# print(multiplied_happiness)

average_happiness = sum(multiplied_happiness) / length_of_employees
# print(average_happiness)

for element in multiplied_happiness:
    if element >= average_happiness:
        counter_for_happy_employees += 1

if counter_for_happy_employees >= length_of_employees // 2:
    print(f"Score: {counter_for_happy_employees}/{length_of_employees}. Employees are happy!")
else:
    print(f"Score: {counter_for_happy_employees}/{length_of_employees}. Employees are not happy!")