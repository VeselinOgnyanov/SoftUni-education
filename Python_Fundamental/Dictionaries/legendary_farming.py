text = input()
material_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
legendary_item = ""
legendary_item_obtained = False

while not legendary_item_obtained:
    text = text.lower().split(" ")
    for index in range(0, len(text), 2):
        key = text[index + 1]
        value = int(text[index])
        if key == "shards" or key == "fragments" or key == "motes":
            material_dict[key] += value
            if material_dict["shards"] >= 250:
                legendary_item_obtained = True
                material_dict["shards"] -= 250
                legendary_item = "shards"
                break
            elif material_dict["fragments"] >= 250:
                legendary_item_obtained = True
                material_dict["fragments"] -= 250
                legendary_item = "fragments"
                break
            elif material_dict["motes"] >= 250:
                legendary_item_obtained = True
                material_dict["motes"] -= 250
                legendary_item = "motes"
                break
        else:
            if text[index + 1] not in junk_dict:
                junk_dict[key] = 0
            junk_dict[key] += value
    if legendary_item_obtained:
        break
    text = input()


if legendary_item == "shards":
    print("Shadowmourne obtained!")
elif legendary_item == "fragments":
    print("Valanyr obtained!")
elif legendary_item == "motes":
    print("Dragonwrath obtained!")
for key, value in material_dict.items():
    print(f"{key}: {value}")
for key, value in junk_dict.items():
    print(f"{key}: {value}")







