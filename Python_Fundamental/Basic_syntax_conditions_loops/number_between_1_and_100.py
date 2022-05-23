current_number = float(input())
while True:
    if (current_number >= 1) and (current_number <= 100):
        print(f"The number {current_number} is between 1 and 100")
        break
    else:
        current_number = float(input())
