import re

text = input()
pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
new_text = re.findall(pattern, text)
new_text = " ".join(new_text)
print(new_text)