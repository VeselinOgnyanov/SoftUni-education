text = input().split(" ")
char_dict = {}
for element in text:
    for char in element:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

for key, value in char_dict.items():
    print(f"{key} -> {value}")

