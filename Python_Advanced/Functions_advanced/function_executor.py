def func_executor(*args):
    resulted_string = ""
    for current_function in args:
        resulted_string += current_function[0].__name__ + " - " + str(current_function[0](*current_function[1])) + "\n"
    return resulted_string


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


