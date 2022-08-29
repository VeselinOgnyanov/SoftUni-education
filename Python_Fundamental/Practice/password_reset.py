password_string = input()
new_password_string = ""
command = input()

while command != "Done":
    command = command.split(" ")
    if command[0] == "TakeOdd":
        for index in range(len(password_string)):
            if index % 2 == 1:
                new_password_string += password_string[index]
        password_string = new_password_string
        new_password_string = ""
        print(password_string)
    elif command[0] == "Cut":
        for index in range(len(password_string)):
            if (index >= int(command[1])) and (index < (int(command[1]) + int(command[2]))):
                pass
            else:
                new_password_string += password_string[index]
        password_string = new_password_string
        new_password_string = ""
        print(password_string)
    else:   # command[0] == "Substitute"
        if command[1] in password_string:
            password_string = password_string.replace(command[1], command[2])
            print(password_string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {password_string}")
