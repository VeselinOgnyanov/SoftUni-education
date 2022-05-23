first_number = int(input())
last_number = int(input())
stop_number = int(input())

for number in range(last_number, first_number - 1, -1):
    if number == stop_number:
        if stop_number % 3 == 0 and stop_number % 2 == 0:
            break
    if number % 3 == 0 and number % 2 == 0:
        print(number, end=" ")