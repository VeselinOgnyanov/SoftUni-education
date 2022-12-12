my_list = input().split()

my_list = [float(elements) for elements in my_list]
my_tuple = tuple(my_list)
unique_list = []

for current_element in my_list:
    if current_element not in unique_list:
        unique_list.append(current_element)

for unique_elements in unique_list:
    current_count_of_unique_element = my_tuple.count(unique_elements)
    print(f"{unique_elements} - {current_count_of_unique_element} times")
