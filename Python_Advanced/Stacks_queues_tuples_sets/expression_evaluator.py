from collections import deque

given_string = deque(input().split())
working_list = []

for _ in range(len(given_string)):
    current_symbol = given_string.popleft()
    if current_symbol == "*":
        first_value = working_list[0]
        for element in range(1, len(working_list)):
            current_value = first_value * working_list[element]
            first_value = current_value
        working_list.clear()
        working_list.append(int(first_value))
    elif current_symbol == "+":
        first_value = working_list[0]
        for element in range(1, len(working_list)):
            current_value = first_value + working_list[element]
            first_value = current_value
        working_list.clear()
        working_list.append(int(first_value))
    elif current_symbol == "-":
        first_value = working_list[0]
        for element in range(1, len(working_list)):
            current_value = first_value - working_list[element]
            first_value = current_value
        working_list.clear()
        working_list.append(int(first_value))
    elif current_symbol == "/":
        first_value = working_list[0]
        for element in range(1, len(working_list)):
            current_value = first_value / working_list[element]
            first_value = current_value
        working_list.clear()
        working_list.append(int(first_value))
    else:
        working_list.append(int(current_symbol))
print(working_list[0])


# # new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # current_value = 0
# # for element in new_list:
# #     if current_value != 0:
# #         current_value -= int(element)
# #     else:
# #         current_value = element
# # print(current_value)
# # print(sum(new_list))

# working_list = [1, 2, 3, 4, 5]
# new_list = [-x for x in working_list[1:]]
# new_sub_list = working_list[0] + [-x for x in working_list[1:]]
# print(new_list)
