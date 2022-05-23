number = int(input())

index0 = number // 100
index1 = number // 10 % 10
index2 = number % 10
# index0 = str(index0)
# index1 = str(index1)
# index2 = str(index2)
# new_number = index2 + index1 + index0
# new_number = int(new_number)
result = 0

for i in range(1, index2 + 1):
    for j in range(1, index1 + 1):
        for k in range(1, index0 + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")