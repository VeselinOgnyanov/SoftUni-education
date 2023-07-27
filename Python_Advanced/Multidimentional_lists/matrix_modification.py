def validating_coordinates(main_matrix, row_to_check, col_to_check):
    if row_to_check >= len(main_matrix) or col_to_check >= len(main_matrix) or \
            row_to_check < 0 or col_to_check < 0:
        return False
    else:
        return True


def printing_matrix(matrix_to_print):
    for i in range(len(matrix_to_print)):
        joined_row = " ".join(map(str, matrix_to_print[i]))
        print(joined_row)


rows = int(input())
matrix = [list(map(int, input().split())) for x in range(rows)]

command = input()
while command != "END":
    split_command = command.split()
    current_row = int(split_command[1])
    current_col = int(split_command[2])
    current_value = int(split_command[3])
    if not validating_coordinates(matrix, current_row, current_col):
        print("Invalid coordinates")
        command = input()
        continue
    if split_command[0] == "Add":
        matrix[current_row][current_col] += current_value
    elif split_command[0] == "Subtract":
        matrix[current_row][current_col] -= current_value
    command = input()

printing_matrix(matrix)