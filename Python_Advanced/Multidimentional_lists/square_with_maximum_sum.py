row, col = input().split(", ")

row = int(row)
col = int(col)
matrix = []
final_result = 0
first_line = []
second_line = []

for _ in range(row):
    current_row = input().split(", ")
    matrix.append(list(map(int, current_row)))

for current_row_index in range(row - 1):
    for current_col_index in range(col - 1):
        buffer_result = ((matrix[current_row_index][current_col_index]) +
                         (matrix[current_row_index][current_col_index + 1])
                         + (matrix[current_row_index + 1][current_col_index]) +
                         (matrix[current_row_index + 1][current_col_index + 1]))
        if buffer_result > final_result:
            first_line = matrix[current_row_index][current_col_index], matrix[current_row_index][current_col_index + 1]
            second_line = matrix[current_row_index + 1][current_col_index],\
                          matrix[current_row_index + 1][current_col_index + 1]
            final_result = buffer_result
            buffer_result = 0

print(*first_line, sep=" ")
print(*second_line, sep=" ")
print(final_result)