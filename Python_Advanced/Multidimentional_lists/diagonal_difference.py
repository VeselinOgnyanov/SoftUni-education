rows_square = int(input())

matrix = [list(map(int, input().split(" "))) for i in range(rows_square)]

primary_diag = []
secondary_diag = []

for index in range(rows_square):
    primary_diag.append(matrix[index][index])
    secondary_diag.append(matrix[index][(rows_square - 1) - index])

pri_print = ", ".join(map(str, primary_diag))
sec_print = ", ".join((map(str, secondary_diag)))

prim_sum = sum(primary_diag)
sec_sum = sum(secondary_diag)
diag_diff = abs(prim_sum - sec_sum)

joined_prim = " +".join(map(str, primary_diag))
joined_sec = " +".join(map(str, secondary_diag))
joined_diff = "|" + str(prim_sum) + "-" + str(sec_sum) + "|"

print(diag_diff)
