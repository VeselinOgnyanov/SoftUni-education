drink = input()
sugar = input()
number_drinks = int(input())
total_price = 0

if drink == "Espresso":
    if sugar == "Without":
        total_price = 0.90 * number_drinks
        total_price *= 0.65
    elif sugar == "Normal":
        total_price = 1.0 * number_drinks
    else:
        total_price = 1.2 * number_drinks
    if number_drinks >= 5:
        total_price *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        total_price = 1.0 * number_drinks
        total_price *= 0.65
    elif sugar == "Normal":
        total_price = 1.2 * number_drinks
    else:
        total_price = 1.6 * number_drinks
else:
    if sugar == "Without":
        total_price = 0.5 * number_drinks
        total_price *= 0.65
    elif sugar == "Normal":
        total_price = 0.6 * number_drinks
    else:
        total_price = 0.7 * number_drinks

if total_price > 15.0:
    total_price *= 0.8

print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")
