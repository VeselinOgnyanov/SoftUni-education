command = input()
words = {}

while command != "end":
    reversed_text = command[:: -1]
    words[command] = reversed_text
    command = input()

for keys, values in words.items():
    print(f"{keys} = {values}")


