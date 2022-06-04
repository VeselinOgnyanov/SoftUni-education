import math

group_size = int(input())
days = int(input())
total_coins = 0
current_count_of_companions = group_size

for days in range(1, days + 1):
    total_coins += 50
    if days % 10 == 0:
        current_count_of_companions -= 2
    if days % 15 == 0:
        current_count_of_companions += 5
    coins_for_food = current_count_of_companions * 2
    total_coins -= coins_for_food
    if days % 3 == 0:
        coins_for_water = current_count_of_companions * 3
        total_coins -= coins_for_water
    if days % 5 == 0:
        bossmonster_coins = current_count_of_companions * 20
        total_coins += bossmonster_coins
        if days % 3 == 0:
            total_coins -= current_count_of_companions * 2

coins_per_companion = math.floor(total_coins / current_count_of_companions)
print(f"{current_count_of_companions} companions received {coins_per_companion} coins each.")
