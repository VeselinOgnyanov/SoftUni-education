row_col = int(input())

matrix = []
result = 0

for _ in range(row_col):
    matrix.append(input().split())

for index in range(row_col):
    result += int(matrix[index][index])

print(result)