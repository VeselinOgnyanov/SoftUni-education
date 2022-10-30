town_people = {}
town_gold = {}

command = input()
while command != "Sail":
    command = command.split("||")
    if command[0] not in town_people:
        town_people[command[0]] = 0
    town_people[command[0]] += int(command[1])
    if command[0] not in town_gold:
        town_gold[command[0]] = 0
    town_gold[command[0]] += int(command[2])
    command = input()

command = input()
while command != "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        town_people[command[1]] -= int(command[2])
        town_gold[command[1]] -= int(command[3])
        print(f"{command[1]} plundered! {command[3]} gold stolen, {command[2]} citizens killed.")
        if town_people[command[1]] <= 0 or town_gold[command[1]] <= 0:
            print(f"{command[1]} has been wiped off the map!")
            town_people.pop(command[1])
            town_gold.pop(command[1])
    elif command[0] == "Prosper":
        if int(command[2]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            town_gold[command[1]] += int(command[2])
            print(f"{command[2]} gold added to the city treasury. {command[1]} now has {town_gold[command[1]]} gold.")
    command = input()
if len(town_people) <= 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(town_people)} wealthy settlements to go to:")
    for towns in town_people:
        print(f"{towns} -> Population: {town_people[towns]} citizens, Gold: {town_gold[towns]} kg")



