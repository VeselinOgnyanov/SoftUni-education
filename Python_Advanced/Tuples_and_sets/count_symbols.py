text = input()
new_text = tuple([x for x in text])

dictionary = {}

for element in new_text:
    if element not in dictionary:
        dictionary[element] = 0
    dictionary[element] = new_text.count(element)

new_dictionary = dict(sorted(dictionary.items()))

for key, value in new_dictionary.items():
    print(f"{key}: {value} time/s")
