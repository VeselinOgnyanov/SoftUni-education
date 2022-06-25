def absolute_value(list_of_numbers):
    list_of_numbers = numbers.split(' ')
    final_list = []
    for element in list_of_numbers:
        element = float(element)
        final_list.append(abs(element))
    return final_list


numbers = input()
print(absolute_value(numbers))
