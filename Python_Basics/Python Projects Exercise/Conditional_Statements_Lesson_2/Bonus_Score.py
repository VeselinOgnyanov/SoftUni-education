number = int(input())
bonus = 0
add_bonus = 0
final_value = 0

if number <= 100:
    bonus = 5
elif number < 1000:
    bonus = number * 0.20
else:
    bonus = number * 0.10

if number % 2 == 0:
    add_bonus = 1
    final_value = number + bonus + add_bonus
elif number % 10 == 5:
    add_bonus = 2
    final_value = number + bonus + add_bonus
else:
    final_value = number + bonus

print(bonus + add_bonus)
print(final_value)