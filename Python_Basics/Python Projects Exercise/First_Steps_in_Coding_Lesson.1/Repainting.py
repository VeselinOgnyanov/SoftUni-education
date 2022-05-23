guard_nylon = 1.50
paint_per_litter = 14.50
paint_thinner_per_litter = 5.00
nylon_bags = 0.40

needed_gurd_nylons = int(input())
needed_paint = int(input())
needed_thinner = int(input())
needed_hours = int(input())

final_nylon_price = (needed_gurd_nylons + 2) * guard_nylon
final_paint_price = (needed_paint + (needed_paint * 0.1)) * paint_per_litter
final_paint_thinner_price = needed_thinner * paint_thinner_per_litter

materials_price = final_paint_price + final_nylon_price + final_paint_thinner_price + 0.40
worker_salary = (materials_price * 0.30) * needed_hours
work_plus_materials = materials_price + worker_salary

print(work_plus_materials)

