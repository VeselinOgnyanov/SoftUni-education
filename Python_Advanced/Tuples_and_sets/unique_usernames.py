number_of_usernames = int(input())
usernames_set = set()
for _ in range(number_of_usernames):
    usernames_set.add(input())
for element in usernames_set:
    print(element)
    