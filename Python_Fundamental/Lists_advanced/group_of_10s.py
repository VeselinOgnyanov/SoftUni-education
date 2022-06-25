import math

sequence = input().split(", ")
integer_sequence = list(map(int, sequence))
max_number = max(integer_sequence)
quantity_of_groups = math.floor(max_number / 10)
previous_group = 0
current_list = []

for current_group in range(1, quantity_of_groups + 1):
    for element in integer_sequence:
        if (element > previous_group * 10) and (element <= (current_group * 10)):
            current_list.append(element)
    previous_group += 1
    print(f"Group of {current_group*10}'s: {current_list}")
    current_list.clear()