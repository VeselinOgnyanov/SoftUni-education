def chars_in_range(first_symbol, final_symbol):
    new_list = []
    for index in range(ord(first_symbol) + 1, ord(final_symbol)):
        new_list.append(chr(index))
    new_string = " ".join(new_list)
    return new_string


first = input()
final = input()

print(chars_in_range(first, final))
