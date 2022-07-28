list_of_chars = input().split(", ")

new_dict = {char: ord(char) for char in list_of_chars}
print(new_dict)

