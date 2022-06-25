def sum_numbers(first, second):
    result = first + second
    return result


def subtract(first, third):
    result = first - third
    return result


def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)
    subtract_sum_minus_third = subtract(sum_of_first_and_second, third)
    result = subtract_sum_minus_third
    return result


first_int = int(input())
second_int = int(input())
third_int = int(input())

print(add_and_subtract(first_int, second_int, third_int))
