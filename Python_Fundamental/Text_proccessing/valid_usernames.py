usernames = input().split(", ")
validated_usernames = []
valid_name = True

for current_username in usernames:
    is_alphanum = False
    if (len(current_username) < 3) or (len(current_username) > 16):
        continue
    if " " in current_username:
        continue
    for current_char in current_username:
        is_alphanum = current_char.isalnum()
        if not is_alphanum and current_char != "-" and current_char != "_":
            valid_name = False
            break
    if valid_name:
        validated_usernames.append(current_username)
    valid_name = True

for current_username in validated_usernames:
    print(current_username)

