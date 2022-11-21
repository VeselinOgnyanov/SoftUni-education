from collections import deque

quantity_of_water = int(input())
people_queue = deque([])

people_names = input()
while people_names != "Start":
    people_queue.append(people_names)
    people_names = input()

command = input()
while command != "End":
    command = command.split()
    if len(command) == 1:
        if int(command[0]) <= quantity_of_water:
            print(f"{people_queue.popleft()} got water")
            quantity_of_water -= int(command[0])
        else:
            print(f"{people_queue[0]} must wait")
            people_queue.popleft()
    # refill
    else:
        quantity_of_water += int(command[1])
    command = input()

print(f"{quantity_of_water} liters left")