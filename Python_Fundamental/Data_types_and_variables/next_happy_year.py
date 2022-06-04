start_year = int(input())
next_year = 0
new_set = set()

while True:
    next_year = start_year + 1
    start_year = str(start_year)
    next_year = str(next_year)
    length_of_start_year = len(start_year)

    for index in range(length_of_start_year):
        new_set.add(next_year[index])

    length_of_new_set = len(new_set)
    if length_of_new_set == length_of_start_year:
        break
    else:
        start_year = int(next_year)
        new_set = set()

print(next_year)
