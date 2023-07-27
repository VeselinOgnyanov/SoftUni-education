import functools


def multiply(*numbers):
    result = functools.reduce(lambda a, b: a * b, numbers)
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))