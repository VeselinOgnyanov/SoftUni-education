city = input()
package = input()
have_vip_discount = input()
days_for_vacation = int(input())

wrong_input = False
total_price = 0

if days_for_vacation > 7:
    days_for_vacation -= 1

if city == "Bansko" or city == "Borovets":
    if package == "noEquipment":
        total_price = days_for_vacation * 80
        if have_vip_discount == "yes":
            total_price *= 0.95
    elif package == "withEquipment":
        total_price = days_for_vacation * 100
        if have_vip_discount == "yes":
            total_price *= 0.90
    else:
        wrong_input = True

elif city == "Varna" or city == "Burgas":
    if package == "noBreakfast":
        total_price = days_for_vacation * 100
        if have_vip_discount == "yes":
            total_price *= 0.93
    elif package == "withBreakfast":
        total_price = days_for_vacation * 130
        if have_vip_discount == "yes":
            total_price *= 0.88
    else:
        wrong_input = True
else:
    wrong_input = True

if wrong_input:
    print("Invalid input!")
elif days_for_vacation < 1:
    print("Days must be positive number!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
