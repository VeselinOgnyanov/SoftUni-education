factor = int(input())
count = int(input())

my_new_list = []

for iterations in range(1, count + 1):
    new_value = factor * iterations
    my_new_list.append(new_value)

my_new_list.sort()
print(my_new_list)
