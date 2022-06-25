train = []
wagons = int(input())
for _ in range(wagons):
    train.append(0)

command = input()
while command != "End":
    command_list = command.split()
    if command_list[0] == "add":
        train[-1] += int(command_list[1])
    elif command_list[0] == "insert":
        number_of_wagon = int(command_list[1])
        train[number_of_wagon] += int(command_list[2])
    elif command_list[0] == "leave":
        number_of_wagon = int(command_list[1])
        train[number_of_wagon] -= int(command_list[2])
    command = input()

print(train)