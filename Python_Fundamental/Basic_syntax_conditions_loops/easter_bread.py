budget = float(input())
price_for_1_kg_flour = float(input())

colored_eggs = 0
price_for_one_loaf = 0
count_loafs = 0

price_for_1_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1_liter_milk = price_for_1_kg_flour * 1.25

while budget > 0:
    price_for_one_loaf = price_for_1_pack_of_eggs + price_for_1_kg_flour + (price_for_1_liter_milk / 4)
    colored_eggs += 3
    budget -= price_for_one_loaf

