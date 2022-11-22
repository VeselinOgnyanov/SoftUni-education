def removing_first_and_last_element(current_list):
    new_list = list(current_list)
    new_list.pop(0)
    new_list.pop(-1)
    return new_list


def removing_first_and_second_element(current_list):
    new_list = list(current_list)
    new_list.pop(0)
    new_list.pop(0)
    return new_list


parentheses = input()
parentheses_list = []
balanced = True

for element in parentheses:
    parentheses_list.append(element)

for _ in range(len(parentheses)):
    if len(parentheses_list) == 1:
        balanced = False
        break
    elif parentheses_list:
        first_element = parentheses_list[0]
        second_element = parentheses_list[1]
        last_element = parentheses_list[-1]
        if first_element == "{":
            if second_element == "}":
                parentheses_list = removing_first_and_second_element(parentheses_list)
            elif last_element == "}":
                parentheses_list = removing_first_and_last_element(parentheses_list)
            else:
                balanced = False
                break
        elif first_element == "[":
            if second_element == "]":
                parentheses_list = removing_first_and_second_element(parentheses_list)
            elif last_element == "]":
                parentheses_list = removing_first_and_last_element(parentheses_list)
            else:
                balanced = False
                break
        elif first_element == "(":
            if second_element == ")":
                parentheses_list = removing_first_and_second_element(parentheses_list)
            elif last_element == ")":
                parentheses_list = removing_first_and_last_element(parentheses_list)
            else:
                balanced = False
                break
        else:
            balanced = False
            break

print("YES" if balanced else "NO")
