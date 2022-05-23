budget = int(input())
command = input()
total_price = 0
overdraft = False
while command != "End":
    command = int(command)
    total_price += command
    if total_price > budget:
        overdraft = True
        break
    command = input()

if overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")



