from collections import deque

parentheses = input()
parentheses_list = []
balanced = True

for element in parentheses:
    parentheses_list.append(element)

for _ in range(len(parentheses)):
    if parentheses_list == 1:
        balanced = False
    if parentheses_list:
        first_element = parentheses_list[0]
        last_element = parentheses_list[-1]
        if first_element in ["{", "(", "["]:
            if last_element == "}":
                if parentheses_list:
                    parentheses_list.pop(0)
                    parentheses_list.pop()
                else:
                    balanced = False
                    break
            elif last_element == "]":
                if parentheses_list:
                    parentheses_list.pop(0)
                    parentheses_list.pop()
                else:
                    balanced = False
                    break
            elif last_element == ")":
                if parentheses_list:
                    parentheses_list.pop(0)
                    parentheses_list.pop()
                else:
                    balanced = False
                    break

print("YES" if balanced else "NO")