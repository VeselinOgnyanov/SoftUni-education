first_sequence = input().split(", ")
sub_sequence = input().split(", ")
final_list = []

for short_element in first_sequence:
    for element in sub_sequence:
        if short_element in element:
            final_list.append(short_element)
            break
print(final_list)