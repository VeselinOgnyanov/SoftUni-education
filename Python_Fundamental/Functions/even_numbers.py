def to_int(number):
    return int(number)


def even_numbers(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


sequence_of_numbers = input()
new_list = sequence_of_numbers.split(" ")
mapped_int_list = list(map(to_int, new_list))
filtered_int_list = list(filter(even_numbers, mapped_int_list))
print(filtered_int_list)
