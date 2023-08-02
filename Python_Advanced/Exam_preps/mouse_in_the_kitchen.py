def moving(direction, start_pos):
    next_position = []
    if direction == "up":
        next_position = [start_pos[0] - 1, start_pos[1]]
    if direction == "down":
        next_position = [start_pos[0] + 1, start_pos[1]]
    if direction == "left":
        next_position = [start_pos[0], start_pos[1] - 1]
    if direction == "right":
        next_position = [start_pos[0], start_pos[1] + 1]
    return next_position


def check_if_in_board(position):
    if 0 <= position[0] < row and 0 <= position[1] < col:
        return False
    else:
        return True


row, col = map(int, input().split(","))
board = [list(input()) for x in range(row)]

start_position = []
next_step = []
number_of_cheeses = 0
mouse_outside = False
cheese_is_eaten = False
mouse_is_trapped = False
mouse_in_danger = False

for r in range(len(board)):
    if "M" in board[r]:
        start_position = [r, board[r].index("M")]

board[start_position[0]][start_position[1]] = "*"

for r in range(row):
    for c in range(col):
        if board[r][c] == "C":
            number_of_cheeses += 1

command = input()

while True:
    if command == "up":
        next_step = moving("up", start_position)
    elif command == "down":
        next_step = moving("down", start_position)
    elif command == "left":
        next_step = moving("left", start_position)
    elif command == "right":
        next_step = moving("right", start_position)
    elif command == "danger":
        mouse_in_danger = True
        break

    if check_if_in_board(next_step):
        mouse_outside = True
        break
    if board[next_step[0]][next_step[1]] == "@":
        command = input()
        continue
    start_position = next_step

    if board[start_position[0]][start_position[1]] == "C":
        number_of_cheeses -= 1
        board[start_position[0]][start_position[1]] = "*"
        if number_of_cheeses == 0:
            cheese_is_eaten = True
            break
    elif board[start_position[0]][start_position[1]] == "T":
        board[start_position[0]][start_position[1]] = "*"
        mouse_is_trapped = True
        break

    command = input()

if mouse_outside:
    print("No more cheese for tonight!")
elif cheese_is_eaten:
    print("Happy mouse! All the cheese is eaten, good night!")
elif mouse_is_trapped:
    print("Mouse is trapped!")
elif mouse_in_danger:
    print("Mouse will come back later!")

board[start_position[0]][start_position[1]] = "M"
for row in board:
    print("".join(row))
