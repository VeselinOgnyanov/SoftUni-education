from collections import deque

list_of_people = input().split()
n_person = int(input())
counter = 0
last_name = False
erased_name = ""

while True:
    if n_person == 1:
        if len(list_of_people) == 1:
            last_name = True
            break
        else:
            que = deque(list_of_people)
            que_removed_person = que.popleft()
            print(f"Removed {que_removed_person}")
            list_of_people = que
    else:
        for index in range(0, len(list_of_people)):
            if len(list_of_people) == 1:
                last_name = True
                break
            else:
                counter += 1
                if counter % n_person == 0:
                    erased_name = list_of_people.pop(index)
                    print(f"Removed {erased_name}")
                    counter = 0
    if last_name:
        break
print(f"Last is {list_of_people[0]}")
