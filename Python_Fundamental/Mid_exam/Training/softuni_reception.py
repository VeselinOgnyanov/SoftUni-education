first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
all_students = int(input())

efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
additional_hours = 0

needed_hours = all_students // efficiency_per_hour
students_left = all_students % efficiency_per_hour
if students_left > 0:
    needed_hours += 1
if needed_hours > 3:
    additional_hours = needed_hours // 3
needed_hours += additional_hours
print(f"Time needed: {needed_hours}h.")
