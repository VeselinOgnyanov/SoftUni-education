days = int(input())
room_type = input()
grade = input()

price_for_nights = 0


if room_type == "room for one person":
    price_for_nights = (days - 1) * 18.00
elif room_type == "apartment":
    price_for_nights = (days - 1) * 25.00
    if days < 10:
        price_for_nights *= 0.70
    elif days <= 15:
        price_for_nights *= 0.65
    else:
        price_for_nights *= 0.50
else:
    price_for_nights = (days - 1) * 35.00
    if days < 10:
        price_for_nights *= 0.90
    elif days <= 15:
        price_for_nights *= 0.85
    else:
        price_for_nights *= 0.80

if grade == "positive":
    price_for_nights *= 1.25
else:
    price_for_nights *= 0.90

print(f"{price_for_nights:.2f}")

