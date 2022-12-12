number_of_names = int(input())
odd_set = set()
even_set = set()

for row in range(1, number_of_names + 1):
    current_name = input()
    current_ascii_value = 0
    for element in current_name:
        current_ascii_value += ord(element)
    new_value = int(current_ascii_value / row)
    if new_value % 2 == 0:
        even_set.add(new_value)
    else:
        odd_set.add(new_value)

if sum(odd_set) == sum(even_set):
    last_set = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    last_set = odd_set.difference(even_set)
elif sum(odd_set) < sum(even_set):
    last_set = odd_set.symmetric_difference(even_set)
result = [str(x) for x in last_set]
print(", ".join(result))
