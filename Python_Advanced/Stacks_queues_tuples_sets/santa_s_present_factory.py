from collections import deque


def popping_items(magic_level_list, materials_for_crafting_list):
    magic_level_list.popleft()
    materials_for_crafting_list.pop()


materials_for_crafting = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

crafted_dictionary = dict()
crafted_dictionary["Doll"] = 0
crafted_dictionary["Wooden train"] = 0
crafted_dictionary["Teddy bear"] = 0
crafted_dictionary["Bicycle"] = 0

while materials_for_crafting and magic_level:
    current_material_for_crafting = materials_for_crafting[-1]
    current_magic_level = magic_level[0]
    total_magic_level = current_magic_level * current_material_for_crafting
    if total_magic_level == 150:
        crafted_dictionary["Doll"] += 1
        popping_items(magic_level, materials_for_crafting)
        continue
    if total_magic_level == 250:
        crafted_dictionary["Wooden train"] += 1
        popping_items(magic_level, materials_for_crafting)
        continue
    if total_magic_level == 300:
        crafted_dictionary["Teddy bear"] += 1
        popping_items(magic_level, materials_for_crafting)
        continue
    if total_magic_level == 400:
        crafted_dictionary["Bicycle"] += 1
        popping_items(magic_level, materials_for_crafting)
        continue
    # match total_magic_level:
    #     case 150:
    #         crafted_dictionary["Doll"] += 1
    #         popping_items(magic_level, materials_for_crafting)
    #         continue
    #     case 250:
    #         crafted_dictionary["Wooden train"] += 1
    #         popping_items(magic_level, materials_for_crafting)
    #         continue
    #     case 300:
    #         crafted_dictionary["Teddy bear"] += 1
    #         popping_items(magic_level, materials_for_crafting)
    #         continue
    #     case 400:
    #         crafted_dictionary["Bicycle"] += 1
    #         popping_items(magic_level, materials_for_crafting)
    #         continue
    if total_magic_level < 0:
        summed_value = current_magic_level + current_material_for_crafting
        popping_items(magic_level, materials_for_crafting)
        materials_for_crafting.append(summed_value)
    elif current_material_for_crafting == 0 or current_magic_level == 0:
        if current_material_for_crafting == 0 and current_magic_level == 0:
            popping_items(magic_level, materials_for_crafting)
        elif current_material_for_crafting == 0:
            materials_for_crafting.pop()
        elif current_magic_level == 0:
            magic_level.popleft()
    else:
        magic_level.popleft()
        materials_for_crafting[-1] += 15

if (crafted_dictionary["Doll"] >= 1 and crafted_dictionary["Wooden train"] >= 1) or \
        (crafted_dictionary["Teddy bear"] >= 1 and crafted_dictionary["Bicycle"] >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_for_crafting:
    materials_for_crafting.reverse()
    left_materials = ", ".join(map(str, materials_for_crafting))
    print(f"Materials left: {left_materials}")
if magic_level:
    left_magic = ", ".join(map(str, magic_level))
    print(f"Magic left: {left_magic}")

sorted_crafted_dictionary = dict(sorted(crafted_dictionary.items(), key=lambda x: x[0]))
# print(sorted_crafted_dictionary)
for current_key, current_value in sorted_crafted_dictionary.items():
    if int(current_value) >= 1:
        print(f"{current_key}: {current_value}")
