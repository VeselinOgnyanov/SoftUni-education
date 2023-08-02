import functools
from functools import reduce


def operate(operator, *numbers):
    result = 0
    if operator == "+":
        result = reduce(lambda a, b: a+b, numbers)
    elif operator == "-":
        result = reduce(lambda a, b: a-b, numbers)
    elif operator == "*":
        result = reduce(lambda a, b: a*b, numbers)
    elif operator == "/":
        result = reduce(lambda a, b: a/b, numbers)
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))