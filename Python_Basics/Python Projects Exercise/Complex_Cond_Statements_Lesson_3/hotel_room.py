month = input()
number_nights = int(input())

price_studio = 0
price_apart = 0
final_price_studio = 0
final_price_apart = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apart = 65
    if 7 < number_nights <= 14:
        price_studio *= 0.95
    elif number_nights > 14:
        price_studio *= 0.70
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apart = 68.70
    if number_nights > 14:
        price_studio *= 0.80
elif month == "July" or month == "August":
    price_studio = 76
    price_apart = 77
if number_nights > 14:
    price_apart *= 0.90

final_price_studio = price_studio * number_nights
final_price_apart = price_apart * number_nights
print(f"Apartment: {final_price_apart:.2f} lv.")
print(f"Studio: {final_price_studio:.2f} lv.")