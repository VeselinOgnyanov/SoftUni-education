total_gold_per_working_days = 0
num_locations = int(input())
for i in range(num_locations):
    aver_gold = float(input())
    working_days = int(input())
    for j in range(working_days):
        gold_per_day = float(input())
        total_gold_per_working_days += gold_per_day
    calculated_aver_gold = total_gold_per_working_days / working_days
    if calculated_aver_gold >= aver_gold:
        print(f"Good job! Average gold per day: {calculated_aver_gold:.2f}.")
    else:
        diff = abs(aver_gold - calculated_aver_gold)
        print(f"You need {diff:.2f} gold.")
    total_gold_per_working_days = 0
