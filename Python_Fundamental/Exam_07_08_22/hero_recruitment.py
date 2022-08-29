command = input()
hero_name_dict = {}

while command != "End":
    command = command.split(" ")
    if command[0] == "Enroll":
        if command[1] in hero_name_dict:
            print(f"{command[1]} is already enrolled.")
        else:
            hero_name_dict[command[1]] = []
    elif command[0] == "Learn":
        if command[1] not in hero_name_dict:
            print(f"{command[1]} doesn't exist.")
        elif command[2] in hero_name_dict[command[1]]:
            print(f"{command[1]} has already learnt {command[2]}.")
        else:
            hero_name_dict[command[1]].append(command[2])
    else:         # Unlearn
        if command[1] not in hero_name_dict:
            print(f"{command[1]} doesn't exist.")
        elif command[2] not in hero_name_dict[command[1]]:
            print(f"{command[1]} doesn't know {command[2]}.")
        else:
            index = hero_name_dict[command[1]].index(command[2])
            hero_name_dict[command[1]].pop(index)
    command = input()

print("Heroes:")
for heroes, spells in hero_name_dict.items():
    spells = ", ".join(spells)
    print(f"== {heroes}: {spells}")


# new_list = ["a", "b", "c"]
# index = new_list.index("b")
# print(index)