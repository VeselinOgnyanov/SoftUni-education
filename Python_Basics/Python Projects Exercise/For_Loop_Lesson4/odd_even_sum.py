count = int(input())
odd_sum = 0
even_sum = 0
for i in range(1, count + 1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
diff = abs(odd_sum - even_sum)
if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")
