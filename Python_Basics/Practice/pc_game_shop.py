def percents(amount, total_amount):
    result = (amount/total_amount) * 100
    return result

number = int(input())

counter_for_hearthstone = 0
counter_for_fortnite = 0
counter_for_overwatch = 0
counter_for_others = 0

for count in range(0, number):
    game_name = input()
    if game_name == "Hearthstone":
        counter_for_hearthstone += 1
    elif game_name == "Fornite":
        counter_for_fortnite += 1
    elif game_name == "Overwatch":
        counter_for_overwatch += 1
    else:
        counter_for_others += 1

percents_hearthstone = percents(counter_for_hearthstone, number)
percents_fortnite = percents(counter_for_fortnite, number)
percents_overwatch = percents(counter_for_overwatch, number)
percents_others = percents(counter_for_others, number)

print(f"Hearthstone - {percents_hearthstone:.2f}%")
print(f"Fornite - {percents_fortnite:.2f}%")
print(f"Overwatch - {percents_overwatch:.2f}%")
print(f"Others - {percents_others:.2f}%")




