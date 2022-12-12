number_of_names = int(input())
names_list = []
for _ in range(number_of_names):
    current_name = input()
    names_list.append(current_name)

new_set = set(names_list)
for element in new_set:
    print(element)
