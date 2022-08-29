import re

text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

searched_list = re.findall(pattern, text, flags=re.I)
print(len(searched_list))
