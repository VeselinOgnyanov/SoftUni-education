budget = float(input())
season = input()
destination = ""
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        budget *= 0.30
    else:
        place = "Hotel"
        budget *= 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        budget *= 0.40
    else:
        place = "Hotel"
        budget *= 0.80
else:
    destination = "Europe"
    place = "Hotel"
    budget *= 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")