flower_type = input()
flower_count = int(input())
budget = int(input())

roses_price = 5.0
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3.0
gladiolus_price = 2.50
final_price = 0

if flower_type == "Roses":
    if flower_count > 80:
        final_price = roses_price * flower_count
        final_price *= 0.90
    else:
        final_price = roses_price * flower_count
elif flower_type == "Dahlias":
    if flower_count > 90:
        final_price = dahlias_price * flower_count
        final_price *= 0.85
    else:
        final_price = dahlias_price * flower_count
elif flower_type == "Tulips":
    if flower_count > 80:
        final_price = tulips_price * flower_count
        final_price *= 0.85
    else:
        final_price = tulips_price * flower_count
elif flower_type == "Narcissus":
    if flower_count < 120:
        final_price = narcissus_price * flower_count
        final_price *= 1.15
    else:
        final_price = narcissus_price * flower_count
else: #Gladiolus
    if flower_count < 80:
        final_price = gladiolus_price * flower_count
        final_price *= 1.20
    else:
        final_price = gladiolus_price * flower_count
difference = abs(budget - final_price)

if budget >= final_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")