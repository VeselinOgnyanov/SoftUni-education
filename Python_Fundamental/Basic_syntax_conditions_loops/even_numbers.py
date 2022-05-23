quantity_numbers = int(input())
odd_number = False
current_number = 0
for i in range(quantity_numbers):
    current_number = int(input())
    if current_number % 2 == 1:
        odd_number = True
        break
    continue
if odd_number:
    print(f"{current_number} is odd!")
else:
    print("All numbers are even.")
        