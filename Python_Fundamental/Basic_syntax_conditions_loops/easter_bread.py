budget = float(input())
price_for_1_kg_flour = float(input())

colored_eggs = 0
price_for_one_loaf = 0
count_loafs = 0

price_for_1_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1_liter_milk = price_for_1_kg_flour * 1.25
price_for_one_loaf = 0

while budget >= price_for_one_loaf:
    price_for_one_loaf = price_for_1_pack_of_eggs + price_for_1_kg_flour + (price_for_1_liter_milk / 4)
    if price_for_one_loaf >= budget:
        break
    colored_eggs += 3
    count_loafs += 1
    if count_loafs % 3 == 0:
        loosed_eggs = count_loafs - 2
        colored_eggs -= loosed_eggs
    budget -= price_for_one_loaf

print(f"You made {count_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

