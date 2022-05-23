days = int(input())
room_type = input()
grade = input()

room_for_one_person = 18.0
apartment = 25.0
president_apartment = 35.0
nights = days - 1
price = 0
all_sum = 0

if room_type == "room for one person":
    price = nights * room_for_one_person
    if grade == "positive":
        price *= 1.25
    else:
        price *= 0.90
elif room_type == "apartment":
    price = nights * apartment
    if days < 10:
        price *= 0.70
    elif 10 < days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.50
    if grade == "positive":
        price *= 1.25
    else:
        price *= 0.90
else:
    price = nights * president_apartment
    if days < 10:
        price *= 0.90
    elif 10 < days <= 15:
        price *= 0.85
    else:
        price *= 0.80
    if grade == "positive":
        price *= 1.25
    else:
        price *= 0.90
print(f"{price:.2f}")