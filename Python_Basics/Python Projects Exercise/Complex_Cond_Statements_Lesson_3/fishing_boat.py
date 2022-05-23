budget = int(input())
season = input()
num_fishers = int(input())

boat_rent = 0
middle_price = 0
final_price = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
else:
    boat_rent = 4200
if num_fishers <= 6:
    middle_price = boat_rent * 0.90
elif 6 < num_fishers <= 11:
    middle_price = boat_rent * 0.85
else:
    middle_price = boat_rent * 0.75
if num_fishers % 2 == 0:
    if season != "Autumn":
        final_price = middle_price * 0.95
    else:
        final_price = middle_price
else:
    final_price = middle_price
difference = abs(budget - final_price)

if budget >= final_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
