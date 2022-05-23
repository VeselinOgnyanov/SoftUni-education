tabs = int(input())
salary = int(input())

current_salary = salary

for i in range(tabs):
    tab_name = input()
    if tab_name == "Facebook":
        current_salary -= 150
        if current_salary <= 0:
            break
    elif tab_name == "Instagram":
        current_salary -= 100
        if current_salary <= 0:
            break
    elif tab_name == "Reddit":
        current_salary -= 50
        if current_salary <= 0:
            break
if current_salary <= 0:
    print("You have lost your salary.")
else:
    print(current_salary)

