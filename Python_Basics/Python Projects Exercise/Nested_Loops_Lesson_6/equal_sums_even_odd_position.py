first_number = int(input())
second_number = int(input())

values_odd = 0
values_even = 0

for current_number in range(first_number, second_number + 1):
    current_number = str(current_number)
    for index, value in enumerate(current_number):
        value = int(value)
        if index % 2 != 0:
            values_even += value
        else:
            values_odd += value
    if values_even == values_odd:
        print(current_number, end=" ")
    values_odd = 0
    values_even = 0

