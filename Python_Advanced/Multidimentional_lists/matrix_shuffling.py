def is_valid(string_to_check):
    validating_string = str(string_to_check).split()
    if validating_string[0] != "swap":
        return False
    elif len(validating_string) > 5 or len(validating_string) <= 4:
        return False
    elif int(validating_string[1]) > rows or int(validating_string[3]) > rows \
            or int(validating_string[2]) > cols or int(validating_string[4]) > cols:
        return False
    elif int(validating_string[1]) < 0 or int(validating_string[3]) < 0 \
            or int(validating_string[2]) < 0 or int(validating_string[4]) < 0:
        return False
    else:
        return True


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for x in range(rows)]

command = input()
while command != "END":
    is_checked = is_valid(command)
    if not is_checked:
        print("Invalid input!")
        command = str(input())
        continue
    command_list = command.split()
    row1, col1, row2, col2 = [int(x) for x in command_list[1:]]
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for element in matrix:
        print(*element, sep=" ")

    command = str(input())


