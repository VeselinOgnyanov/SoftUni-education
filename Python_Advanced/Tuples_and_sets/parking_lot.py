number_of_commands = int(input())
park_lot = set()

for _ in range(number_of_commands):
    current_commands = input().split(", ")
    if current_commands[0] == "IN":
        park_lot.add(current_commands[1])
    else:
        park_lot.discard(current_commands[1])

if len(park_lot) == 0:
    print("Parking Lot is Empty")
else:
    for el in park_lot:
        print(el)
