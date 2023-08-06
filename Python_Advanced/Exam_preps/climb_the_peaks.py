def remove_food_stamina():
    food_portions.pop(0)
    stamina.pop(0)


food_portions = list(map(int, input().split(", ")))
stamina = list(map(int, input().split(", ")))

food_portions.reverse()
current_sum = 0
peaks_conquered = []
day_passed = 0

peaks_dict = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

for _ in range(7):
    if peaks_conquered == 5:
        break
    current_sum = food_portions[0] + stamina[0]
    remove_food_stamina()
    for key, value in peaks_dict.items():
        if current_sum >= value:
            peaks_conquered.append(key)
            peaks_dict.pop(key)
            break
        else:
            break

string_to_print = ""
string_to_print += "Conquered peaks:" + "\n"
for peak in peaks_conquered:
    string_to_print += peak + "\n"

if len(peaks_conquered) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK" + "\n" + string_to_print)
elif len(peaks_conquered) < 5:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if peaks_conquered:
        print(string_to_print)



