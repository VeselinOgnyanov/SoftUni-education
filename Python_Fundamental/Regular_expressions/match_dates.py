import re

text = input()
pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"

new_text = re.findall(pattern, text)
# new_text = ", ".join(new_text)

for elements in new_text:
    print(f"Day: {elements[0]}, Month: {elements[2]}, Year: {elements[3]}")
