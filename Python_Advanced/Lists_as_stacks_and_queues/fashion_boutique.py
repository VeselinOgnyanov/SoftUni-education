stack_of_clothes = input().split()
capacity_of_a_rack = int(input())

current_capacity = capacity_of_a_rack
capacity_is_full = False
number_of_racks = 1

while stack_of_clothes:
    current_capacity -= int(stack_of_clothes[-1])
    if current_capacity < 0:
        number_of_racks += 1
        current_capacity = capacity_of_a_rack
    else:
        stack_of_clothes.pop()

print(number_of_racks)
