budget = float(input())
number_of_nights = int(input())
price_per_one_night = float(input())
percent_for_add_spends = int(input())

if number_of_nights > 7:
    price_per_one_night = price_per_one_night * 0.95

price_for_nights = number_of_nights * price_per_one_night
price_for_add_spends = budget * (percent_for_add_spends / 100)
total_price = price_for_nights + price_for_add_spends
diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")