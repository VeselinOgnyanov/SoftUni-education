def even_odd(*args):
    command = args[-1]
    elements = []
    final_list = []
    for element_index in range(len(args) - 1):
        elements.append(args[element_index])
    if command == "even":
        final_list = list(filter(lambda x: (x % 2 == 0), elements))
    elif command == "odd":
        final_list = list(filter(lambda x: (x % 2 == 1), elements))
    return final_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))