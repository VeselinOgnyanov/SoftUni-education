people_to_elevate = int(input())
elevator_capacity = int(input())

needed_courses = people_to_elevate % elevator_capacity
result = people_to_elevate // elevator_capacity

if needed_courses == 0:
    print(result)
else:
    result += 1
    print(result)
