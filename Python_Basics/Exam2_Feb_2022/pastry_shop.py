cake = input()
number_cakes = int(input())
day = int(input())
price_per_cake = 0
if cake == "Cake":
    if day <= 15:
        price_per_cake = 24
    else:
        price_per_cake = 28.70
elif cake == "Souffle":
    if day <= 15:
        price_per_cake = 6.66
    else:
        price_per_cake = 9.80
else:
    if day <= 15:
        price_per_cake = 12.60
    else:
        price_per_cake = 16.98

price_for_all_cakes = price_per_cake * number_cakes

if day <= 22:
    if 100 <= price_for_all_cakes <= 200:
        price_for_all_cakes *= 0.85
    elif price_for_all_cakes > 200:
        price_for_all_cakes *= 0.75
    if day <= 15:
        price_for_all_cakes *= 0.90

print(f"{price_for_all_cakes:.2f}")
