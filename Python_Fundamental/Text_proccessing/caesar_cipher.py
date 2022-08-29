text = input()
ciphered_text = ""

for character in text:
    ciphered_character = ord(character) + 3
    ciphered_text += chr(ciphered_character)

print(ciphered_text)