divisor = int(input())
boundary = int(input())

max_divisor = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        max_divisor = i

print(max_divisor)