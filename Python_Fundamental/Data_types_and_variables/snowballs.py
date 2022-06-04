number_of_snowballs = int(input())
current_snowball_value = 0
highest_weight_of_snowball = 0
highest_time_to_target = 0
highest_quality = 0

for balls in range(1, number_of_snowballs + 1):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality = int(input())

    snowball_value = (weight_of_snowball / time_to_target) ** quality
    if snowball_value > current_snowball_value:
        current_snowball_value = int(snowball_value)
        highest_weight_of_snowball = weight_of_snowball
        highest_time_to_target = time_to_target
        highest_quality = quality

print(f"{highest_weight_of_snowball} : {highest_time_to_target} = {current_snowball_value} ({highest_quality})")


