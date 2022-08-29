import re

text = input()
pattern = r"\d"
emoji_pattern = r"(\*\*|\:\:)\b[A-Z][a-z]{2,}\b\1"
last_result = 1
current_sum = 0
cool_threshold = 0

found_digits = re.findall(pattern, text)

threshold = [int(x) for x in found_digits]
for index in range(len(threshold)):
    cool_threshold = last_result * threshold[index]
    last_result = cool_threshold
found_emojis = re.finditer(emoji_pattern, text)
found_list = [x.group() for x in found_emojis]

print(f"Cool threshold: {last_result}")
print(f"{len(found_list)} emojis found in the text. The cool ones are:")

for elements in found_list:
    for current_symbol in elements:
        if current_symbol != ":" and current_symbol != "*":
            current_sum += ord(current_symbol)
    if current_sum > last_result:
        print(elements)
        current_sum = 0
    else:
        current_sum = 0
        continue
