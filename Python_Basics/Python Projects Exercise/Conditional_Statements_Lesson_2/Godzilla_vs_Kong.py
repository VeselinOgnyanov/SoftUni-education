budget = float(input())
statists = int(input())
price_clothes_per_one = float(input())

decor = budget * 0.10
clothes = statists * price_clothes_per_one

if statists >= 150:
    clothes *= 0.90

needed_sum = decor + clothes
money_left = needed_sum - budget
if needed_sum > budget:
    print(f"Not enough money! \nWingard needs {money_left:.2f} leva more.")
else:
    money_left = abs(money_left)
    print(f"Action! \nWingard starts filming with {money_left:.2f} leva left.")
