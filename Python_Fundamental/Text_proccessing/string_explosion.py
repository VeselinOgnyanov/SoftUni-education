text = input()
bomb_strength = 0
new_text = ""

for index in range(len(text)):
    if bomb_strength > 0 and text[index] != ">":
        bomb_strength -= 1
        continue
    elif text[index] == ">":
        bomb_strength += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)
