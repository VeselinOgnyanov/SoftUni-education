number_of_commands = int(input())
employee_dict = {}

for _ in range(number_of_commands):
    command = input().split(" ")
    if command[0] == "register":
        if command[1] in employee_dict.keys():
            print(f"ERROR: already registered with plate number {employee_dict[command[1]]}")
        else:
            employee_dict[command[1]] = command[2]
            print(f"{command[1]} registered {employee_dict[command[1]]} successfully")
    elif command[0] == "unregister":
        if command[1] not in employee_dict.keys():
            print(f"ERROR: user {command[1]} not found")
        else:
            employee_dict.pop(command[1])
            print(f"{command[1]} unregistered successfully")

for key, value in employee_dict.items():
    print(f"{key} => {value}")
