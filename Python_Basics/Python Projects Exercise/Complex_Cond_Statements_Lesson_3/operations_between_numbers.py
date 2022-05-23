num1 = int(input())
num2 = int(input())
operator = input()
result = 0
odd = ""
cannot_divide = False
if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        odd = "even"
    else:
        odd = "odd"
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        odd = "even"
    else:
        odd = "odd"
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        odd = "even"
    else:
        odd = "odd"
elif operator == "/":
    if num2 == 0:
        cannot_divide = True
    else:
        result = num1 / num2
elif operator == "%":
    if num2 == 0:
        cannot_divide = True
    else:
        result = num1 % num2

if operator == "+" or operator == "-" or operator == "*":
    print(f"{num1} {operator} {num2} = {result} - {odd}")
elif operator == "/":
    if cannot_divide:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} / {num2} = {result:.2f}")
elif operator == "%":
    if cannot_divide:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} % {num2} = {result}")
