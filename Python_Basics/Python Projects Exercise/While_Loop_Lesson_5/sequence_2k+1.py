number = int(input())
first_num = 1
current_sum = 0
while current_sum <= number:
    print(first_num)
    current_sum = first_num * 2 + 1
    first_num = current_sum
