number_of_lines = int(input())

current_matrix = []
flattered_matrix = []

for _ in range(number_of_lines):
    current_matrix = list(map(int, input().split(", ")))
    flattered_matrix.extend(current_matrix)

print(flattered_matrix)