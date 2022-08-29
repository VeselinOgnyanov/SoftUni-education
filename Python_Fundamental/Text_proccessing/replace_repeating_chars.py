text = input()
non_repeating_chars = []
current_char = ""
last_char = ""
for index in range(len(text)):
    current_char = text[index]
    if last_char != current_char:
        last_char = current_char
        non_repeating_chars.append(last_char)

# print(non_repeating_chars)

non_repeating_string = "".join(non_repeating_chars)
print(non_repeating_string)