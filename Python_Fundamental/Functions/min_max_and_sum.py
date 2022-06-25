numbers = input()
int_list = numbers.split(" ")
int_list = list(map(lambda x: int(x), int_list))

min_val = min(int_list)
max_val = max(int_list)
sum_of_list = sum(int_list)

print(f"The minimum number is {min_val}")
print(f"The maximum number is {max_val}")
print(f"The sum number is {sum_of_list}")