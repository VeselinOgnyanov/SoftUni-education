hour = int(input())
minutes = int(input())
add_min = 15

if minutes + add_min >= 60:
    hour += 1
    if hour == 24:
        hour = 0
    minutes = (minutes + add_min) % 60
    if minutes >= 10:
        minutes = minutes
    else:
        minutes = f"0{minutes}"
elif minutes + add_min < 10:
    hour = hour
    minutes += add_min
    minutes = f"0{minutes}"
elif minutes + add_min < 60:
    hour = hour
    minutes += add_min

print(f"{hour}:{minutes}")