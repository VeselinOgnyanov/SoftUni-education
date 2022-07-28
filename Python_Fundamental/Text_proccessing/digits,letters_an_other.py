text = input()

digits = ""
chars = ""
other_chars = ""

for element in text:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        chars += element
    else:
        other_chars += element

print(digits)
print(chars)
print(other_chars)
