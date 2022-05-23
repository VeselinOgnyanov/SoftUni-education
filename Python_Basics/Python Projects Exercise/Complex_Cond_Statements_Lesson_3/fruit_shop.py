fruit = input()
week_day = input()
quantity = float(input())

banana = 0
apple = 0
orange = 0
grapefruit = 0
kiwi = 0
pineapple = 0
grapes = 0
price = 0
is_valid = True
if week_day == "Monday" or week_day == "Tuesday" or week_day == "Thursday" or week_day == "Wednesday" or week_day == "Friday":
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        is_valid = False
elif week_day == "Saturday" or week_day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        is_valid = False
else:
    is_valid = False
if is_valid:
    print(f"{price:.2f}")
else:
    print("error")