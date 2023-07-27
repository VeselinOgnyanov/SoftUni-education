board_rows = int(input())

board = [list(input()) for i in range(board_rows)]
removed_knights = 0
knight_directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
)

while True:
    total_attacks = 0
    position_of_strongest_night = []

    for row in range(board_rows):
        for col in range(board_rows):

            if board[row][col] == "K":
                current_attack_count = 0
                start_position = [row, col]

                for cur_direction in knight_directions:
                    next_row = start_position[0] + cur_direction[0]
                    next_col = start_position[1] + cur_direction[1]
                    next_position = [next_row, next_col]

                    if (next_row >= 0 and next_col >= 0) and (next_row < board_rows and next_col < board_rows):
                        if board[next_row][next_col] == "K":
                            current_attack_count += 1

                if current_attack_count > total_attacks:
                    total_attacks = current_attack_count
                    position_of_strongest_night = start_position

    if total_attacks == 0:
        break
    else:
        board[position_of_strongest_night[0]][position_of_strongest_night[1]] = "0"
        removed_knights += 1

print(removed_knights)