first_line = input().split(", ")
first_line = list(map(int, first_line))

rows, columns = first_line
matrix = []
result = 0
for _ in range(rows):
    matrix.append(input().split())

for column_index in range(columns):
    for row_index in range(rows):
        current_number_of_matrix = int(matrix[row_index][column_index])
        result += current_number_of_matrix
    print(result)
    result = 0
