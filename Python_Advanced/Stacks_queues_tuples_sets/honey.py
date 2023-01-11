from collections import deque

working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
honey_making_process = deque(input().split())
current_honey_in_hive = 0

while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        current_bee = working_bees.popleft()
        current_nectar = nectar.pop()
        current_operation = str(honey_making_process.popleft())
        if current_operation == "+":
            current_honey_in_hive += abs((current_nectar + current_bee))
        elif current_operation == "-":
            current_honey_in_hive += abs((current_nectar - current_bee))
        elif current_operation == "*":
            current_honey_in_hive += abs((current_nectar * current_bee))
        elif current_operation == "/":
            current_honey_in_hive += abs((current_nectar / current_bee))
    else:
        nectar.pop()

print(f"Total honey made: {current_honey_in_hive}")
if working_bees:
    final_bees = ", ".join(map(str, working_bees))
    print(f"Bees left: {final_bees}")
if nectar:
    final_nectar = ", ".join(map(str,nectar))
    print(f"Nectar left: {final_nectar}")
