gifts_to_buy = input()
first_list = gifts_to_buy.split()


command = input()
while command != "No Money":
    new_list = command.split()
    if new_list[0] == "OutOfStock":
        for index in range(len(first_list)):
            lookup_word = new_list[1]
            if first_list[index] == lookup_word:
                first_list[index] = 'None'
    elif new_list[0] == "Required":
        lookup_word = new_list[1]
        index_for_replace = int(new_list[2])
        if (index_for_replace > 0) and (index_for_replace < len(first_list)):
            first_list[index_for_replace] = lookup_word
    elif new_list[0] == "JustInCase":
        first_list.pop()
        first_list.append(new_list[1])
    command = input()

for element in first_list:
    if element == 'None':
        first_list.remove(element)

final_string = ' '.join(first_list)
print(final_string)


