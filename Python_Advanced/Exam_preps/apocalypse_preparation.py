def remove_values():
    textiles.pop(0)
    medicaments.pop(0)


textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))
medicaments.reverse()

items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    sum = textiles[0] + medicaments [0]
    if sum == 30:
        items["Patch"] += 1
        remove_values()
    elif sum == 40:
        items["Bandage"] += 1
        remove_values()
    elif sum == 100:
        items["MedKit"] += 1
        remove_values()
    elif sum > 100:
        items["MedKit"] += 1
        buffer = abs(sum - 100)
        remove_values()
        medicaments[0] += buffer
    else:
        textiles.pop(0)
        medicaments[0] += 10

items = dict(sorted(items.items(), key= lambda x: (-x[1], x[0])))

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not (medicaments):
    print("Medicaments are empty.")

for key, value in items.items():
    if value > 0:
        print(f"{key} - {value}")

if medicaments:
    string_medicaments = list(map(str, medicaments))
    joined_med = ", ".join(string_medicaments)
    print(f"Medicaments left: {joined_med}")
if textiles:
    string_textiles = list(map(str, textiles))
    joined_textiles = ", ".join(string_textiles)
    print(f"Textiles left: {joined_textiles}")