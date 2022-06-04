number_of_pours = int(input())
max_capacity = 255
current_capacity = 0
for _ in range(number_of_pours):
    liters_of_water = int(input())
    if current_capacity + liters_of_water > max_capacity:
        current_capacity = current_capacity
        print("Insufficient capacity!")
        continue
    else:
        current_capacity += liters_of_water

print(current_capacity)
