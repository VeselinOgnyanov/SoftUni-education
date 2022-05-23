import math

height_of_the_wall = int(input())
width_of_the_wall = int(input())
percent_of_non_painted = int(input())

area_for_painting = height_of_the_wall * width_of_the_wall * 4
percent_of_non_painted /= 100
percent_of_non_painted *= area_for_painting
area_for_painting -= percent_of_non_painted
area_for_painting = math.ceil(area_for_painting)

paint_is_enough = False
have_left_paint = False
current_area = 0
diff = 0
command = input()
while command != "Tired!":
    current_liters = int(command)
    current_area += current_liters
    if area_for_painting - current_area == 0:
        paint_is_enough = True
        break
    elif area_for_painting - current_area < 0:
        have_left_paint = True
        break
    command = input()


if area_for_painting > current_area:
    diff = area_for_painting - current_area
    print(f"{diff} quadratic m left.")
elif paint_is_enough:
    print("All walls are painted! Great job, Pesho!")
elif have_left_paint:
    diff = abs(area_for_painting - current_area)
    print(f"All walls are painted and you have {diff} l paint left!")