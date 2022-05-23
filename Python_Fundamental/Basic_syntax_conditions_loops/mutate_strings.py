first_string = input()
second_string = input()
length = len(first_string)
current_string = first_string
for i in range(length):
    right_side = first_string[i+1: length + 1: 1]
    left_side = second_string[0: i+1: 1]
    new_string = left_side + right_side
    if current_string == new_string:
        continue
    current_string = new_string
    print(left_side + right_side)

