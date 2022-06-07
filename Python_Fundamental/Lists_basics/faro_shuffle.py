first_deck = input()
shuffle_quantity = int(input())

first_list = first_deck.split()
left_list = []
right_list = []
last_shuffle = []
length_of_first_list = len(first_list)
for _ in range(shuffle_quantity):
    for iterations in range(0, length_of_first_list // 2):
        left_list.append(first_list[iterations])
    for iterations in range(length_of_first_list // 2, length_of_first_list):
        right_list.append(first_list[iterations])
    first_list.clear()
    for iterations in range(0, length_of_first_list // 2):
        last_shuffle.append(left_list[iterations])
        last_shuffle.append(right_list[iterations])
    first_list = last_shuffle
    left_list.clear()
    right_list.clear()

print(last_shuffle)
