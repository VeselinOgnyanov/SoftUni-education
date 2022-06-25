def rounding_string_to_list(selected_string):
    new_list = selected_string.split(" ")
    for index in range(len(new_list)):
        new_list[index] = float(new_list[index])
        new_list[index] = round(new_list[index])
    return new_list


new_string = input()
print(rounding_string_to_list(new_string))

