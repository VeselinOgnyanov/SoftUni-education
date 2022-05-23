number = int(input())

is_special = False
counter = 0
for num in range(1111, 9999 + 1):
    num = str(num)
    for index, value in enumerate(num):
        value = int(value)
        if value == 0:
            continue
        if number % value == 0:
            counter += 1
        if counter == 4:
            is_special = True
        if is_special:
            print(num, end=" ")
            is_special = False
    counter = 0

