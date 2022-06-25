rooms = int(input())
total_chair = 0
total_people = 0
in_need_of_chairs = False
for current_room in range(1, rooms + 1):
    current_list = input().split()
    number_of_chairs = len(current_list[0])
    current_people = int(current_list[1])
    if number_of_chairs >= current_people:
        total_chair += number_of_chairs
        total_people += current_people
    else:
        needed_chairs = abs(number_of_chairs - current_people)
        print(f"{needed_chairs} more chairs needed in room {current_room}")
        in_need_of_chairs = True

total_free_chairs = abs(total_chair - total_people)
if not in_need_of_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

