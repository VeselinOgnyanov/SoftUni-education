number_of_strings = int(input())
searched_word = input()
full_list = []
searched_list = []
for _ in range(number_of_strings):
    string = input()
    full_list.append(string)
    if searched_word in string:
        searched_list.append(string)

print(full_list)
print(searched_list)
