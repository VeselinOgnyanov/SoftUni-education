actor_name = input()
start_points = float(input())
number_judges = int(input())

total_judge_points = start_points
diff = 0
is_nominated = False
for i in range(number_judges):
    judge_name = input()
    judge_points = float(input())
    mid_points = (len(judge_name) * judge_points) / 2
    total_judge_points += mid_points
    if total_judge_points >= 1250.5:
        is_nominated = True
        break
    else:
        diff = abs(total_judge_points - 1250.5)

if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_judge_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")





