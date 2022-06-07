string = input()
my_list = string.split()
my_negative_list = []

for index in range(len(my_list)):
    my_negative_list.append((-int(my_list[index])))

print(my_negative_list)
