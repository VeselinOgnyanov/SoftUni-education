count_number = int(input())

range1 = 0  # < 200
range2 = 0  # 200 <= num <= 399 or num <= 399
range3 = 0  # 400 <= num <= 599 or num <= 599
range4 = 0  # 600 <= num <= 799 or num <= 799
range5 = 0  # num >= 800
percent_range_1 = 0
percent_range_2 = 0
percent_range_3 = 0
percent_range_4 = 0
percent_range_5 = 0

for i in range(count_number):
    number = int(input())
    if number < 200:
        range1 += 1
    elif number <= 399:
        range2 += 1
    elif number <= 599:
        range3 += 1
    elif number <= 799:
        range4 += 1
    else:
        range5 +=1
percent_range_1 = range1 / count_number * 100
percent_range_2 = range2 / count_number * 100
percent_range_3 = range3 / count_number * 100
percent_range_4 = range4 / count_number * 100
percent_range_5 = range5 / count_number * 100

print(f"{percent_range_1:.2f}%")
print(f"{percent_range_2:.2f}%")
print(f"{percent_range_3:.2f}%")
print(f"{percent_range_4:.2f}%")
print(f"{percent_range_5:.2f}%")
