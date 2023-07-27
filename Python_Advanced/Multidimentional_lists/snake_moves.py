rows, cols = [int(x) for x in input().split()]
snake_string = str(input())

multiplied_string = snake_string * (rows * cols)
counter = 1
for current_row in range(rows):
    current_string = multiplied_string[current_row * cols:cols * counter]
    if counter % 2 == 0:
        print(current_string[::-1])
    else:
        print(current_string)
    counter += 1
