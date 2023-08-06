def move(direction, start_step):
    next_step = []
    if direction == "up":
        next_step = [start_step[0] - 1, start_step[1]]
    elif direction == "down":
        next_step = [start_step[0] + 1, start_step[1]]
    elif direction == "left":
        next_step = [start_step[0], start_step[1] - 1]
    elif direction == "right":
        next_step = [start_step[0], start_step[1] + 1]
    return next_step


def move_is_valid(current_move):
    if not rows > current_move[0] >= 0 or not cols > current_move[1] >= 0:
        return False
    else:
        return True


rows, cols = [int(x) for x in input().split(" ")]

playground = []
initial_position = []
moves_made = 0
touched_opponent = 0

for row in range(rows):
    c_row = input().split()
    playground.append(c_row)
    if "B" in c_row:
        initial_position = [row, c_row.index("B")]
        playground[initial_position[0]][initial_position[1]] = "-"


command = input()
while command != "Finish":
    next_move = move(command, initial_position)
    if move_is_valid(next_move):
        if playground[next_move[0]][next_move[1]] == "O":
            command = input()
            continue
        elif playground[next_move[0]][next_move[1]] == "P":
            touched_opponent += 1
            moves_made += 1
            if touched_opponent == 3:
                break
            playground[next_move[0]][next_move[1]] = "-"
        elif playground[next_move[0]][next_move[1]] == "-":
            moves_made += 1
        initial_position = next_move
    else:
        command = input()
        continue
    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponent} Moves made: {moves_made}")

