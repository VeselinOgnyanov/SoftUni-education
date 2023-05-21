number_of_square_matrix_rows = int(input())

matrix = []
found_element =False
position_of_element = []

for _ in range(number_of_square_matrix_rows):
    current_row = input()
    matrix.append(current_row)

wanted_element = input()

for row_index in range(number_of_square_matrix_rows):
    for col_index in range(number_of_square_matrix_rows):
        current_element = matrix[row_index][col_index]
        if current_element == wanted_element:
            position_of_element.append(row_index)
            position_of_element.append(col_index)
            found_element = True
            break
    if found_element:
        break

if found_element:
    joined_position_of_elements = ", ".join(map(str, position_of_element))
    print(f"({joined_position_of_elements})")
else:
    print(f"{wanted_element} does not occur in the matrix")