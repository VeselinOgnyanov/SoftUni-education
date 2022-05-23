count_chicken_meal = int(input())
count_fish_meal = int(input())
count_vegan_meal = int(input())

chicken_price = 10.35 * count_chicken_meal
fish_price = 12.40 * count_fish_meal
vegan_price = 8.15 * count_vegan_meal

price = chicken_price + fish_price + vegan_price
desert = price * 0.20

full_price = price + desert + 2.50

print(full_price)