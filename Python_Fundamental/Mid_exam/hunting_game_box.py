days_of_the_adventure = int(input())
number_of_player = int(input())
group_energy = float(input())
water_per_day_for_person = float(input())
food_per_day_for_one_person = float(input())

all_water = days_of_the_adventure * number_of_player * water_per_day_for_person
all_food = days_of_the_adventure * number_of_player * food_per_day_for_one_person
current_water = 0
current_food = 0
current_energy = 0
not_enough_energy = False

for days in range(1, days_of_the_adventure + 1):
    lost_energy = float(input())
    current_energy = group_energy - lost_energy
    # days_passed += 1
    if current_energy > 0:
        if days % 2 == 0:
            current_energy *= 1.05
            current_water = all_water * 0.7
            all_water = current_water
        if days % 3 == 0:
            current_food = all_food / number_of_player
            all_food -= current_food
            current_energy *= 1.1
        group_energy = current_energy
    else:
        not_enough_energy = True
        break

if not not_enough_energy:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {all_food:.2f} food and {all_water:.2f} water.")