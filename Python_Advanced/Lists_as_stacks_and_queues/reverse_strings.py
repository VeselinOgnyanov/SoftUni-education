new_string = input()
current_stack = []

for element in new_string:
    current_stack.append(element)

while len(current_stack) > 0:
    print(str(current_stack.pop()), end="")
    