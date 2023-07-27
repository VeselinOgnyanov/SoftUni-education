rows, cols = [int(x) for x in input().split()]
matrix = []

for current_row in range(rows):
    matrix_row = [(chr(97 + current_row) + chr(97 + x + current_row) + chr(97 + current_row)) for x in range(cols)]
    matrix.append(matrix_row)

for element in matrix:
    print(" ".join(element))