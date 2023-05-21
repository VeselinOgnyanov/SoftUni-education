rows_columns = input().split(", ")

rows, columns = map(int, rows_columns)
matrix = []
result = 0

for _ in range(rows):
    current_row = input().split(", ")
    current_row = list(map(int, current_row))
    matrix.append(current_row)
    for index in range(columns):
        result += current_row[index]

print(result)
print(matrix)