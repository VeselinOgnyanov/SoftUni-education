floors = int(input())
rooms = int(input())

for num_floors in range(floors, 0, -1):
    for num_rooms in range(0, rooms):
        if num_floors == floors:
            print(f"L{num_floors}{num_rooms} ", end="")
        elif num_floors % 2 != 0:
            print(f"A{num_floors}{num_rooms} ", end="")
        else:
            print(f"O{num_floors}{num_rooms} ", end="")
    print()