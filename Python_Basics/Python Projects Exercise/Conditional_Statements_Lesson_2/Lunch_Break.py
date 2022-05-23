import math

serial_name = input()
duration = int(input())
duration_break_time = int(input())

lunch_break = duration_break_time * 0.125
relax_time = duration_break_time * 0.25
free_time_for_watch = duration_break_time - (lunch_break + relax_time)
minutes_left = math.ceil(abs(free_time_for_watch - duration))
if free_time_for_watch >= duration:
    print(f"You have enough time to watch {serial_name} and left with {minutes_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {minutes_left} more minutes.")