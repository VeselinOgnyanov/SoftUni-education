import re

text = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
new_text = re.findall(pattern, text)
new_text = ", ".join(new_text)
print(new_text)