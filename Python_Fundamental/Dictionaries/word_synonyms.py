number_of_word_synonyms = int(input())

dict_of_synonyms = {}

for _ in range(number_of_word_synonyms):
    key_word = input()
    value_word = input()
    if key_word not in dict_of_synonyms:
        dict_of_synonyms[key_word] = []
    dict_of_synonyms[key_word].append(value_word)

for key, value in dict_of_synonyms.items():
    joined_string = ", ".join(value)
    print(f"{key} - {joined_string}")




