number_of_orders = int(input())
current_price_per_capsule = 0
current_days = 0
current_capsules_per_day = 0
total_price = 0
for orders in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule < 0.01) or (price_per_capsule > 100.00):
        current_price_per_capsule = 0
        current_days = 0
        current_capsules_per_day = 0
        continue
    else:
        current_price_per_capsule = price_per_capsule
    if (days < 1) or (days > 31):
        current_price_per_capsule = 0
        current_days = 0
        current_capsules_per_day = 0
        continue
    else:
        current_days = days
    if (capsules_per_day < 1) or (capsules_per_day > 2000):
        current_price_per_capsule = 0
        current_days = 0
        current_capsules_per_day = 0
        continue
    else:
        current_capsules_per_day = capsules_per_day
    price_per_day = current_price_per_capsule * current_capsules_per_day * current_days
    print(f"The price for the coffee is: ${price_per_day:.2f}")
    total_price += price_per_day

print(f"Total: ${total_price:.2f}")
