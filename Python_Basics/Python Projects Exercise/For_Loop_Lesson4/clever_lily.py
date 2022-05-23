age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())

birthday_money = 0
birthday_toys = 0
stolen_money = 0
total_birthday_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        birthday_money += 10
        stolen_money += 1
        total_birthday_money += birthday_money
    else:
        birthday_toys += 1
total_price_toys = birthday_toys * toy_price
spent_sum = (total_birthday_money - stolen_money) + total_price_toys
money_left = spent_sum - laundry_machine_price
difference = abs(spent_sum - laundry_machine_price)
if spent_sum >= laundry_machine_price:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {difference:.2f}")
