string_of_numbers = input()
quantity_of_numbers_to_be_removed = int(input())

list_of_numbers = string_of_numbers.split()

for index in range(len(list_of_numbers)):
    list_of_numbers[index] = int(list_of_numbers[index])

for iteration in range(quantity_of_numbers_to_be_removed):
    smallest_number = min(list_of_numbers)
    list_of_numbers.remove(smallest_number)

for index in range(len(list_of_numbers)):
    list_of_numbers[index] = str(list_of_numbers[index])

separator = ", "

final_string = separator.join(list_of_numbers)
print(final_string)

