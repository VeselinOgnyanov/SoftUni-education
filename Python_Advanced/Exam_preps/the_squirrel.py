def move(direction, first_step):
    current_step = []
    if direction == "up":
        current_step = [first_step[0] - 1, first_step[1]]
    if direction == "down":
        current_step = [first_step[0] + 1, first_step[1]]
    if direction == "left":
        current_step = [first_step[0], first_step[1] - 1]
    if direction == "right":
        current_step = [first_step[0], first_step[1] + 1]
    return current_step


row_col = int(input())
command_line = input().split(", ")
nuts_collected = 0
all_nuts = 0
field = [list(input()) for x in range(row_col)]
sq_on_trap = False
out_of_field = False
all_nuts_collected = False

initial_step = []

for row in range(row_col):
    if "s" in field[row]:
        initial_step = [row, field[row].index("s")]
        break

field[initial_step[0]][initial_step[1]] = "*"

for row in field:
    for el in row:
        if el == "h":
            all_nuts += 1

for current_direction in command_line:
    next_step = move(current_direction, initial_step)
    if not 0 <= next_step[0] < row_col or not 0 <= next_step[1] < row_col:
        # step outside
        print("The squirrel is out of the field.")
        out_of_field = True
        break
    elif field[next_step[0]][next_step[1]] == "h":
        nuts_collected += 1
        if nuts_collected >= 3:
            all_nuts_collected = True
            print("Good job! You have collected all hazelnuts!")
            break
    elif field[next_step[0]][next_step[1]] == "*":
        initial_step = next_step
        continue
    elif field[next_step[0]][next_step[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        sq_on_trap = True
        break
    initial_step = next_step

if nuts_collected < 3 and not sq_on_trap and not out_of_field and not all_nuts_collected:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {nuts_collected}")
