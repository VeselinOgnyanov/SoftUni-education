rows = int(input())

matrix = []

for _ in range(rows):
    current_row = input().split(", ")
    current_row = list(map(int, current_row))
    buffer_matrix = list(filter(lambda x: x % 2 == 0, current_row))
    matrix.append(buffer_matrix)

print(matrix)

