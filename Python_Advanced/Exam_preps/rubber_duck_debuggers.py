programmers_time = list(map(int, input().split()))
numbers_of_tasks = list(map(int, input().split()))
numbers_of_tasks.reverse()

ducks_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmers_time:
    calculated_result = programmers_time[0] * numbers_of_tasks[0]
    if calculated_result <= 60:
        ducks_dict["Darth Vader Ducky"] += 1
        programmers_time.pop(0)
        numbers_of_tasks.pop(0)
    elif calculated_result <= 120:
        ducks_dict["Thor Ducky"] += 1
        programmers_time.pop(0)
        numbers_of_tasks.pop(0)
    elif calculated_result <= 180:
        ducks_dict["Big Blue Rubber Ducky"] += 1
        programmers_time.pop(0)
        numbers_of_tasks.pop(0)
    elif calculated_result <= 240:
        ducks_dict["Small Yellow Rubber Ducky"] += 1
        programmers_time.pop(0)
        numbers_of_tasks.pop(0)
    else:
        numbers_of_tasks[0] = numbers_of_tasks[0] - 2
        buffer = programmers_time.pop(0)
        programmers_time.append(buffer)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducks_dict.items():
    print(f"{key}: {value}")


