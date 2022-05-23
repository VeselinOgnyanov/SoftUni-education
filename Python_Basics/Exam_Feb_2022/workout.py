import math

num_days = int(input())
first_day_km = float(input())
total_km = first_day_km
km = 0
overall_km = 0
for i in range(num_days):
    percent = int(input())
    km = total_km + (total_km * (percent / 100))
    total_km = km
    overall_km += total_km
    # print(total_km)
overall_km += first_day_km

if overall_km >= 1000:
    more_km = math.ceil(overall_km - 1000)
    print(f"You've done a great job running {more_km} more kilometers!")
else:
    diff = abs(1000 - overall_km)
    diff = math.ceil(diff)
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")