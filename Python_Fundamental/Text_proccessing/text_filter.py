banned_words = input().split(", ")
text = input()

for current_banned_word in banned_words:
    while current_banned_word in text:
        text = text.replace(current_banned_word, ("*" * len(current_banned_word)))

print(text)