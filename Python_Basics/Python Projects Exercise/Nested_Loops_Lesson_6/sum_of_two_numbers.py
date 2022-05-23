first_number = int(input())
second_number = int(input())
magic_number = int(input())

counter_combinations = 0
combination_number = 0
combination_found = False

for number_1 in range(first_number, second_number + 1):
    for number_2 in range(first_number, second_number + 1):
        counter_combinations += 1
        result = number_1 + number_2
        if result == magic_number:
            combination_number = counter_combinations
            combination_found = True
            break
    if combination_found:
        break
if combination_number == 0:
    print(f"{counter_combinations} combinations - neither equals {magic_number}")
else:
    print(f"Combination N:{combination_number} ({number_1} + {number_2} = {magic_number})")



