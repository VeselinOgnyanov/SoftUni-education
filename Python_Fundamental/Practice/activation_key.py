raw_key = input()
command = input()

sliced_string = ""
upper_string = ""
lower_string = ""

while command != "Generate":
    split_command = command.split(">>>")
    if split_command[0] == "Contains":
        if split_command[1] in raw_key:
            print(f"{raw_key} contains {split_command[1]}.")
        else:
            print("Substring not found!")
    elif split_command[0] == "Flip":
        if split_command[1] == "Upper":
            for index in range(len(raw_key)):
                if (index >= int(split_command[2])) and (index < int(split_command[3])):
                    upper_char = raw_key[index].upper()
                    upper_string += upper_char
                else:
                    upper_string += raw_key[index]
            raw_key = upper_string
            upper_string = ""
            print(raw_key)
        else:       # flip lower
            for index in range(len(raw_key)):
                if (index >= int(split_command[2])) and (index < int(split_command[3])):
                    lower_char = raw_key[index].lower()
                    lower_string += lower_char
                else:
                    lower_string += raw_key[index]
            raw_key = lower_string
            lower_string = ""
            print(raw_key)
    else:           # slice command
        for index in range(len(raw_key)):
            is_alpha = raw_key[index].isalpha()
            if (index >= int(split_command[1])) and (index < int(split_command[2])) and is_alpha:
                continue
            else:
                sliced_string += raw_key[index]
        raw_key = sliced_string
        sliced_string = ""
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")
