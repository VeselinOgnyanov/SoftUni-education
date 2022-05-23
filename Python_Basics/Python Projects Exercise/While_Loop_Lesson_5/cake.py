lenth = int(input())
width = int(input())

command = input()
volume = lenth * width
difference = 0
needed_pieces = False

while command != "STOP":
    command = int(command)
    volume -= command
    if volume <= 0:
        volume = abs(volume)
        needed_pieces = True
        break
    command = input()

if needed_pieces:
    print(f"No more cake left! You need {volume} pieces more.")
else:
    print(f"{volume} pieces are left.")