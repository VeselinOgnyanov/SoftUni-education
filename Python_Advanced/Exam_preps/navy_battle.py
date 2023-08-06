def move(direction, current_pos):
    new_pos = []
    if direction == "up":
        new_pos = current_pos[0] - 1, current_pos[1]
    elif direction == "down":
        new_pos = current_pos[0] + 1, current_pos[1]
    elif direction == "left":
        new_pos = current_pos[0], current_pos[1] - 1
    elif direction == "right":
        new_pos = current_pos[0], current_pos[1] + 1
    return new_pos


size_of_matrix = int(input())
matrix = [list(input()) for x in range(size_of_matrix)]

initial_pos = []

for row_num in range(size_of_matrix):
    if "S" in matrix[row_num]:
        initial_pos = [row_num, matrix[row_num].index("S")]
        matrix[initial_pos[0]][initial_pos[1]] = "-"
        break

mines_hit = 0
destroyed_cruisers = 0
all_cruises_destroyed = False
defeat_by_mines = False


while True:
    command = input()
    next_pos = move(command, initial_pos)
    if matrix[next_pos[0]][next_pos[1]] == "-":
        initial_pos = next_pos
        continue
    elif matrix[next_pos[0]][next_pos[1]] == "*":
        matrix[next_pos[0]][next_pos[1]] = "-"
        mines_hit += 1
    elif matrix[next_pos[0]][next_pos[1]] == "C":
        matrix[next_pos[0]][next_pos[1]] = "-"
        destroyed_cruisers += 1
    initial_pos = next_pos
    if destroyed_cruisers == 3:
        all_cruises_destroyed = True
        break
    elif mines_hit == 3:
        defeat_by_mines = True
        break

matrix[initial_pos[0]][initial_pos[1]] = "S"


matrix_for_print = ""
for row in matrix:
    matrix_for_print += "".join(row) + "\n"

if all_cruises_destroyed:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!" + "\n" + matrix_for_print)
elif defeat_by_mines:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{initial_pos[0]}, {initial_pos[1]}]!" + "\n" + matrix_for_print)
