command = input()
total_money = 0
while command != "NoMoreMoney":
    command = float(command)
    if command < 0:
        print("Invalid operation!")
        break
    else:
        total_money += command
        print(f"Increase: {command:.2f}")
        command = input()
print(f"Total: {total_money:.2f}")