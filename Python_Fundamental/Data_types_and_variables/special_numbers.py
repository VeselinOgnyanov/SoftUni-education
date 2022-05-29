a = int(input())
current_result = 0
for i in range(1, a + 1):
    i = str(i)
    for index, number in enumerate(i):
        number = int(number)
        current_result += number

    if current_result == 5 or current_result == 7 or current_result == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
    current_result = 0

