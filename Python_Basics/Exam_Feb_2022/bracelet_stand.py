casual_money_per_day = float(input())
earning_money_per_day = float(input())
expenses_for_5_days = float(input())
present_price = float(input())

casual_money_for_5_days = casual_money_per_day * 5
earned_money_for_5_days = earning_money_per_day * 5

current_money = casual_money_for_5_days + earned_money_for_5_days
current_money = current_money - expenses_for_5_days
diff = abs(current_money - present_price)

if current_money >= present_price:
    print(f"Profit: {current_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")