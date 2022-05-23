import sys

count = int(input())
sum = 0
max_num = -sys.maxsize
for i in range(count):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number
diff = abs(max_num - (sum - max_num))
if (sum - max_num) == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {diff}")
