needed_money = float(input())
current_money = float(input())
days = 0
spend_counter = 0
spend_warning = False
while current_money < needed_money:
    action = input()
    money = float(input())
    days += 1
    if action == "save":
        current_money += money
        spend_counter = 0
    else:
        current_money -= money
        if current_money <= 0:
            current_money = 0
        spend_counter += 1
    if spend_counter == 5:
        spend_warning = True
        break
if spend_warning:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")