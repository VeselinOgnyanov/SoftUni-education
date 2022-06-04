number_of_letters = int(input())

for i in range(number_of_letters):
    for o in range(number_of_letters):
        for p in range(number_of_letters):
            print(f"{chr(97+i)}{chr(97+o)}{chr(97+p)}")
        