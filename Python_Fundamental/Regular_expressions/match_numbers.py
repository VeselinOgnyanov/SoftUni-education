import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)*(\.\d+)?($|(?=\s))"

new_text = re.finditer(pattern, text)
# new_text = " ".join(new_text)

for elements in new_text:
    print(elements.group(), end=" ")

