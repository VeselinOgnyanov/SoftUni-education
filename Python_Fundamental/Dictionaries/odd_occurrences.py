sequence_of_words = input().lower().split(" ")

dictionary = {}
odd_dictionary = {}
for word in sequence_of_words:
    if word not in dictionary.keys():
        dictionary[word] = 0
    dictionary[word] += 1

for elements, values in dictionary.items():
    if values % 2 == 1:
        odd_dictionary[elements] = values

for odd_key in odd_dictionary:
    print(odd_key, end=" ")


