city = input()
trades = float(input())

commission = 0
is_valid = True

if city == "Sofia":
    if 0 <= trades <= 500:
        commission = trades * 0.05
    elif 500 < trades <= 1000:
        commission = trades * 0.07
    elif 1000 < trades <= 10000:
        commission = trades * 0.08
    elif trades > 10000:
        commission = trades * 0.12
    else:
        is_valid = False
elif city == "Varna":
    if 0 <= trades <= 500:
        commission = trades * 0.045
    elif 500 < trades <= 1000:
        commission = trades * 0.075
    elif 1000 < trades <= 10000:
        commission = trades * 0.1
    elif trades > 10000:
        commission = trades * 0.13
    else:
        is_valid = False
elif city == "Plovdiv":
    if 0 <= trades <= 500:
        commission = trades * 0.055
    elif 500 < trades <= 1000:
        commission = trades * 0.080
    elif 1000 < trades <= 10000:
        commission = trades * 0.12
    elif trades > 10000:
        commission = trades * 0.145
    else:
        is_valid = False
else:
    is_valid = False
if is_valid:
    print(f"{commission:.2f}")
else:
    print("error")
