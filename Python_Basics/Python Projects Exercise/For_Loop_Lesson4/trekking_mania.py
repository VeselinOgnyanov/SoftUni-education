number_groups = int(input())

total_people = 0
people_musala = 0
people_monblan =0
people_kilimadjaro =0
people_k2 = 0
people_everest = 0
for i in range(number_groups):
    number_people = int(input())
    if number_people <= 5:
        people_musala += number_people
    elif number_people <= 12:
        people_monblan += number_people
    elif number_people <= 25:
        people_kilimadjaro += number_people
    elif number_people <= 40:
        people_k2 += number_people
    else:
        people_everest += number_people
total_people = people_musala + people_monblan + people_kilimadjaro + people_k2 + people_everest
percent_musala = people_musala / total_people * 100
percent_monblan = people_monblan / total_people * 100
percent_kilimandjaro = people_kilimadjaro / total_people * 100
percent_k2 = people_k2 / total_people * 100
percent_everest = people_everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")