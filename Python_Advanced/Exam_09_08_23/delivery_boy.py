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


def in_boundaries_of_neighbourhood(current_pos):
    if not rows > current_pos[0] >= 0 or not cols > current_pos[1] >= 0:
        return False
    else:
        return True


rows, cols = map(int, input().split(" "))
neighborhood = [list(input()) for x in range(rows)]

initial_position = []
pizza_delivered = False

for current_row in range(rows):
    if "B" in neighborhood[current_row]:
        initial_position = [current_row, neighborhood[current_row].index("B")]
        first_initial_position = [current_row, neighborhood[current_row].index("B")]
        break

while True:
    command = input()
    next_pos = move(command, initial_position)
    if in_boundaries_of_neighbourhood(next_pos):
        if neighborhood[next_pos[0]][next_pos[1]] == "*":
            continue
        elif neighborhood[next_pos[0]][next_pos[1]] == "-":
            neighborhood[next_pos[0]][next_pos[1]] = "."
        elif neighborhood[next_pos[0]][next_pos[1]] == "P":
            neighborhood[next_pos[0]][next_pos[1]] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        elif neighborhood[next_pos[0]][next_pos[1]] == "A":
            neighborhood[next_pos[0]][next_pos[1]] = "P"
            print("Pizza is delivered on time! Next order...")
            pizza_delivered = True
            break
        initial_position = next_pos[0], next_pos[1]
    else:
        print("The delivery is late. Order is canceled.")
        neighborhood[first_initial_position[0]][first_initial_position[1]] = " "
        break

if pizza_delivered:
    neighborhood[first_initial_position[0]][first_initial_position[1]] = "B"

for r in neighborhood:
    print("".join(r))

