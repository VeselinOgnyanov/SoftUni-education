number = int(input())
counter = 0
result = 0
for i in range(0, number + 1):
    for j in range(0, number + 1):
        for z in range(0, number + 1):
            result = i + j + z
            if result == number:
                counter += 1
print(counter)
