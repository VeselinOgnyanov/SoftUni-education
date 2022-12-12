number = int(input())
chemical_set = set()

for _ in range(number):
    new_line = input().split()
    for el in new_line:
        chemical_set.add(el)

for ele in chemical_set:
    print(ele)