string_of_integers = input()
beggars = int(input())

list_of_all_profits = string_of_integers.split(", ")
list_of_all_profits_as_int = []
list_of_separate_profits = []
total_sum_for_beggars = 0
counter = 0

for elements in list_of_all_profits:
    list_of_all_profits_as_int.append(int(elements))

while counter < beggars:
    for index in range(counter, len(list_of_all_profits_as_int), beggars):
        current_sum_for_beggar = list_of_all_profits_as_int[index]
        total_sum_for_beggars += current_sum_for_beggar
    list_of_separate_profits.append(total_sum_for_beggars)
    counter += 1
    total_sum_for_beggars = 0

print(list_of_separate_profits)
