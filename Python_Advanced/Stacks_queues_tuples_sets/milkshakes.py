from collections import deque

chocolates_list = deque(map(int, input().split(", ")))
cup_of_milks_list = deque(map(int, input().split(", ")))

already_made_milkshakes = 0

current_chocolate = 0
current_milkshake = 0
chocolate_is_empty = False
milk_is_empty = False
needed_shakes_done = False

biggest_list = max(len(chocolates_list), len(cup_of_milks_list))

for _ in range(biggest_list):
    if chocolates_list:
        current_chocolate = chocolates_list[-1]
        if cup_of_milks_list:
            current_milkshake = cup_of_milks_list[0]
        else:
            milk_is_empty = True
            break
    else:
        chocolate_is_empty = True
        break
    if current_chocolate == current_milkshake:
        chocolates_list.pop()
        cup_of_milks_list.popleft()
        already_made_milkshakes += 1
        if already_made_milkshakes >= 5:
            needed_shakes_done = True
            break
    elif current_chocolate <= 0 or current_milkshake <= 0:
        if current_chocolate <= 0:
            chocolates_list.remove(current_chocolate)
        if current_milkshake <= 0:
            cup_of_milks_list.remove(current_milkshake)
    else:
        currently_removed_milk_cup = cup_of_milks_list.popleft()
        cup_of_milks_list.append(currently_removed_milk_cup)
        chocolates_list[-1] -= 5

if needed_shakes_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_list:
    left_chocolate = ", ".join(map(str, chocolates_list))
    print(f"Chocolate: {left_chocolate}")
else:
    print("Chocolate: empty")
if cup_of_milks_list:
    left_milk = ", ".join(map(str, cup_of_milks_list))
    print(f"Milk: {left_milk}")
else:
    print("Milk: empty")

