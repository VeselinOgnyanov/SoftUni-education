number = int(input())
powered_num = 0
for i in range(0, number+1):
    if i % 2 == 0:
        powered_num = 2**i
        print(powered_num)