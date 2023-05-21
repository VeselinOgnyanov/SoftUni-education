row, col = input().split(" ")

row = int(row)
col = int(col)
matrix = []
final_result = 0

for _ in range(row):
    current_row = input().split(" ")
    matrix.append(current_row)

for row_index in range(row - 1):
    for col_index in range(col - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] ==\
                matrix[row_index + 1][col_index + 1]:
            final_result += 1

print(final_result)