empty_stack = []
times_to_repeat = int(input())
max_stack = []
min_stack = []
last_stack = []
last_string = ""


def min_number(iterable_min_stack):
    min_number_in_stack = min(iterable_min_stack)
    return min_number_in_stack


def max_number(iterable_max_stack):
    max_number_in_stack = max(iterable_max_stack)
    return max_number_in_stack


for _ in range(times_to_repeat):
    command = input().split()
    if command[0] == "1":                       # '1 {number}' – push the number (integer) into the stack
        empty_stack.append(command[1])
    elif command[0] == "2":                     # '2' – delete the number at the top of the stack
        if empty_stack:
            empty_stack.pop()
    elif command[0] == "3":                     # '3' – print the maximum number in the stack
        if empty_stack:
            print(max_number(empty_stack))
    else:                                       # '4' – print the minimum number in the stack
        if empty_stack:
            print(min_number(empty_stack))

for _ in range(len(empty_stack)):
    last_element = empty_stack.pop()
    last_stack.append(last_element)

for element in last_stack:
    last_string += element + ", "
last_string_length = len(last_string) - 2
print(last_string[0:last_string_length])
