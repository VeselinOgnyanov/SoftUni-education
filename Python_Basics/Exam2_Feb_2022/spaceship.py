import math

ship_wide = float(input())
ship_length = float(input())
ship_high = float(input())
middle_high_astronauts = float(input())

ship_volume = ship_high * ship_wide * ship_length
volume_per_room = 2 * 2 * (middle_high_astronauts + 0.40)

num_rooms = ship_volume / volume_per_room
num_rooms = math.floor(num_rooms)

if num_rooms < 3:
    print("The spacecraft is too small.")
elif num_rooms <= 10:
    print(f"The spacecraft holds {num_rooms} astronauts.")
else:
    print("The spacecraft is too big.")

