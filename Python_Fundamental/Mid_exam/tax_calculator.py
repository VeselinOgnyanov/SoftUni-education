car_list = input().split(">>")
overall_tax = 0
for car in car_list:
    new_car_list = str(car).split()
    for element in new_car_list:
        if element == "family":
            family_tax = 50 - (int(new_car_list[1]) * 5)
            additional_family_tax = ((int(new_car_list[2]) // 3000) * 12)
            all_family_tax = family_tax + additional_family_tax
            overall_tax += all_family_tax
            print(f"A {element} car will pay {all_family_tax:.2f} euros in taxes.")
            break
        elif element == "heavyDuty":
            heavy_duty_tax = 80 - (int(new_car_list[1]) * 8)
            additional_heavy_duty_tax = ((int(new_car_list[2]) // 9000) * 14)
            all_heavy_duty_tax = heavy_duty_tax + additional_heavy_duty_tax
            overall_tax += all_heavy_duty_tax
            print(f"A {element} car will pay {all_heavy_duty_tax:.2f} euros in taxes.")
            break
        elif element == "sports":
            sports_tax = 100 - (int(new_car_list[1]) * 9)
            additional_sports_tax = ((int(new_car_list[2]) // 2000) * 18)
            all_sports_tax = sports_tax + additional_sports_tax
            overall_tax += all_sports_tax
            print(f"A {element} car will pay {all_sports_tax:.2f} euros in taxes.")
            break
        else:
            print("Invalid car type.")
            break
print(f"The National Revenue Agency will collect {overall_tax:.2f} euros in taxes.")