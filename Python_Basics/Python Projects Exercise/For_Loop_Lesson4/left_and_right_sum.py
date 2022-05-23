number = int(input())
left_sum = 0
right_sum = 0

for i in range(number):
    left_number = int(input())
    left_sum += left_number
for i in range(number):
    right_number = int(input())
    right_sum += right_number
diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
