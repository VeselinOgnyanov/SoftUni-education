main_list = input().split("|")

global_list = []

for index in range(len(main_list) - 1, -1, -1):
    current_row = main_list[index].split()
    global_list.extend(current_row)

print(" ".join(global_list))
