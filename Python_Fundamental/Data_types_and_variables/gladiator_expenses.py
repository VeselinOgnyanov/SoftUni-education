lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
total_broken_shields = 0
broken_armor = 0

for current_lost in range(1, lost_fight_count + 1):
    if current_lost % 2 == 0:
        broken_helmet += 1
    if current_lost % 3 == 0:
        broken_sword += 1
        if current_lost % 2 == 0:
            broken_shield += 1
            total_broken_shields += 1
            if broken_shield == 2:
                broken_armor += 1
                broken_shield = 0


expenses = broken_helmet * helmet_price + broken_sword * sword_price + total_broken_shields * shield_price \
           + broken_armor\
           * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
