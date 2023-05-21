rows_square = int(input())

matrix = [list(map(int, input().split(", "))) for i in range(rows_square)]

primary_diag = []
secondary_diag = []

for index in range(rows_square):
    primary_diag.append(matrix[index][index])
    secondary_diag.append(matrix[index][(rows_square - 1) - index])

pri_print = ", ".join(map(str, primary_diag))
sec_print = ", ".join((map(str, secondary_diag)))

print(f"Primary diagonal: {pri_print}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {sec_print}. Sum: {sum(secondary_diag)}")




