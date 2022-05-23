x = int(input())
y = int(input())
z = int(input())

box_volume = 1
room_space = x * y * z
command = input()
no_space = False

while command != "Done":
    command = int(command)
    room_space -= command
    if room_space <= 0:
        no_space = True
        break
    command = input()
if no_space:
    print(f"No more free space! You need {abs(room_space)} Cubic meters more.")
else:
    print(f"{room_space} Cubic meters left.")