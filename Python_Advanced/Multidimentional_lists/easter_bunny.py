size_of_the_field = int(input())

field = [list(input().split()) for i in range(size_of_the_field)]
bunny_position = []
best_path = []
best_direction = ""
max_collected_eggs = 0

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(size_of_the_field):
    if "B" in field[row]:
        col = field[row].index("B")
        bunny_position = [row, col]

for direction, step in directions.items():
    current_direction_eggs = 0
    current_path = []
    start_position = bunny_position
    current_step_left_right = int(start_position[1])
    current_step_up_down = int(start_position[0])
    current_direction = ""
    if direction == "right":
        while True:
            next_step = int(current_step_left_right + step[1])
            if next_step <= 0 or next_step >= len(field) or field[bunny_position[0]][next_step] == "X":
                break
            current_step_left_right += 1
            current_direction_eggs += int(field[start_position[0]][next_step])
            current_path.append([bunny_position[0], next_step])
            current_direction = "right"
    elif direction == "left":
        while True:
            next_step = int(current_step_left_right + step[1])
            if next_step <= 0 or next_step >= len(field) or field[bunny_position[0]][next_step] == "X":
                break
            current_step_left_right -= 1
            current_direction_eggs += int(field[start_position[0]][next_step])
            current_path.append([bunny_position[0], next_step])
            current_direction = "left"
    elif direction == "up":
        while True:
            next_step = int(current_step_up_down + step[0])
            if next_step <= 0 or next_step >= len(field) or field[next_step][start_position[1]] == "X":
                break
            current_step_up_down -= 1
            current_direction_eggs += int(field[next_step][start_position[1]])
            current_path.append([next_step, bunny_position[1]])
            current_direction = "up"
    elif direction == "down":
        while True:
            next_step = int(current_step_up_down + step[0])
            if next_step <= 0 or next_step >= len(field) or field[next_step][start_position[1]] == "X":
                break
            current_step_up_down += 1
            current_direction_eggs += int(field[next_step][start_position[1]])
            current_path.append([next_step, bunny_position[1]])
            current_direction = "down"
    if current_direction_eggs > max_collected_eggs:
        max_collected_eggs = current_direction_eggs
        best_path = current_path.copy()
        current_path.clear()
        best_direction = current_direction

print(best_direction)
for e in best_path:
    print(e)
print(max_collected_eggs)


