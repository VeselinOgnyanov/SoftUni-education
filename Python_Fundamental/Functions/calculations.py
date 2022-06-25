def multiply(a, b):
    result = int(a * b)
    print(result)


def divide(a, b):
    result = int(a / b)
    print(result)


def add(a, b):
    result = int(a + b)
    print(result)


def subtract(a, b):
    result = int(a - b)
    print(result)


operator = input()
parameter_one = int(input())
parameter_two = int(input())

if operator == "multiply":
    multiply(parameter_one, parameter_two)
elif operator == "divide":
    divide(parameter_one, parameter_two)
elif operator == "add":
    add(parameter_one, parameter_two)
elif operator == "subtract":
    subtract(parameter_one, parameter_two)
