length_of_set_one, length_of_set_two = input().split()
set_one = set()
set_two = set()

for _ in range(int(length_of_set_one)):
    set_one.add(input())


for _ in range(int(length_of_set_two)):
    set_two.add(input())

diff_set = set(set_one.intersection(set_two))
for el in diff_set:
    print(el)