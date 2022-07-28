usernames = input().split(", ")
validated_usernames = []

for current_username in usernames:
    if (len(current_username) >= 3) and (len(current_username) <= 16):
        for single_char in current_username:
            if (single_char != single_char.isdigit()) and (single_char != single_char.isalpha()) and (single_char != "_") and (single_char != "-"):
                break
        if " " not in current_username:
            validated_usernames.append(current_username)

print(validated_usernames)
