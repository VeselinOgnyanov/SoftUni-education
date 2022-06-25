to_do_list = [0] * 10

command = input()
while command != "End":
    split_command = command.split("-")
    importance = split_command[0]
    note = split_command[1]
    to_do_list[int(importance) - 1] = note
    command = input()
new_list = [s for s in to_do_list if s != 0]
print(new_list)