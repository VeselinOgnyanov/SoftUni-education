monster_armour = list(map(int, input().split(",")))
soldier_damage = list(map(int, input().split(",")))
soldier_damage.reverse()

monsters_killed = 0

while monster_armour and soldier_damage:
    current_monster = monster_armour[0]
    current_soldier_damage = soldier_damage[0]
    buffer_damage = abs(current_soldier_damage - current_monster)

    if current_soldier_damage >= current_monster:
        monster_armour.pop(0)
        soldier_damage[0] -= current_monster
        if len(soldier_damage) > 1:
            soldier_damage[1] += buffer_damage
        monsters_killed += 1
        soldier_damage.pop(0)
    else:
        monster_armour[0] -= soldier_damage[0]
        soldier_damage.pop(0)
        monster_buffer = monster_armour.pop(0)
        monster_armour.append(monster_buffer)

if not monster_armour:
    print("All monsters have been killed!")
if not soldier_damage:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")