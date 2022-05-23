wanted_profit = float(input())
command = input()
result = 0
diff = 0
target_acquired = False

while command != "Party!":
    number_of_cocktail = int(input())

    name_len = len(command)
    current_result = name_len * number_of_cocktail
    if current_result % 2 == 1:
        current_result *= 0.75
    result += current_result

    if wanted_profit > result:
        diff = wanted_profit - result
        target_acquired = False
    else:
        diff = abs(wanted_profit - result)
        target_acquired = True
        break

    command = input()

if target_acquired:
    print("Target acquired.")
else:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {result:.2f} leva.")