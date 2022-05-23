import math

number_people = int(input())
enter_tax = float(input())
price_per_one_deck_chair = float(input())
price_per_umbrella = float(input())

numbers_of_umbrellas = math.ceil(number_people / 2)
people_for_deck_chair = math.ceil(number_people * 0.75)

tax_for_people = number_people * enter_tax
tax_for_chairs = people_for_deck_chair * price_per_one_deck_chair
tax_for_umbrellas = numbers_of_umbrellas * price_per_umbrella

final_tax = tax_for_people + tax_for_chairs + tax_for_umbrellas
print(f"{final_tax:.2f} lv.")


