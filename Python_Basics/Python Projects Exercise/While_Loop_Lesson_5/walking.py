goal_steps = 10000
command = input()
current_steps = 0
total_steps = 0
steps_reached = False
difference = 0
while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= goal_steps:
        steps_reached = True
        break
    else:
        command = input()
if command == "Going home":
    last_steps = int(input())
    total_steps += last_steps
    if total_steps >= goal_steps:
        steps_reached = True
difference = abs(total_steps - goal_steps)
if steps_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")


