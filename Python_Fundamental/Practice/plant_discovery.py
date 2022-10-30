number = int(input())
plant_rarity_rating_dict = {}

for _ in range(number):
    plant_rarity_command = input().split("<->")
    plant_rarity_rating_dict[plant_rarity_command[0]] = {"rarity": plant_rarity_command[1], "rating": []}

command = input()
while command != "Exhibition":
    split_command = command.split(": ")
    second_split = str(split_command[1])
    second_split = second_split.split(" - ")
    if second_split[0] not in plant_rarity_rating_dict:
        print("error")
        command = input()
        continue
    if split_command[0] == "Rate":
        plant_rarity_rating_dict[second_split[0]]["rating"].append(second_split[1])
    elif split_command[0] == "Update":
        plant_rarity_rating_dict[second_split[0]]["rarity"] = second_split[1]
    else:            # situation for split_command[0] == "Reset"
        if split_command[1] not in plant_rarity_rating_dict:
            print("error")
            command = input()
            continue
        else:
            plant_rarity_rating_dict[split_command[1]]["rating"] = ["0"]
    command = input()

print("Plants for the exhibition:")
for key in plant_rarity_rating_dict.keys():
    rarity = int(plant_rarity_rating_dict[key]["rarity"])
    rating = [int(n) for n in plant_rarity_rating_dict[key]["rating"]]
    if len(rating) == 0:
        rating = 0
    else:
        rating = sum(rating) / len(rating)
    print(f"- {key}; Rarity: {rarity}; Rating: {rating:.2f}")
