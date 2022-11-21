text = input()

parenthesis_stack = []

for index in range(0, len(text)):
    if text[index] == "(":
        parenthesis_stack.append(index)
    elif text[index] == ")":
        last_index = index
        print(text[parenthesis_stack[-1]:last_index + 1])
        parenthesis_stack.pop()
