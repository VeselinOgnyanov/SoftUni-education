first_line = set(input().split())
second_line = set(input().split())

# print(first_line)
# print(second_line)

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for times in range(2, len(command)):
                first_line.add(command[times])
        else:                                               # command[1] == "Second"
            for times in range(2, len(command)):
                second_line.add(command[times])
    elif command[0] == "Remove":
        if command[1] == "First":
            for times in range(2, len(command)):
                if command[times] in first_line:
                    first_line.remove(command[times])
        else:                                               # command[1] == "Second"
            for times in range(2, len(command)):
                if command[times] in second_line:
                    second_line.remove(command[times])
    elif command[0] == "Check":
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print("True")
        else:
            print("False")

first_sorted_line = map(str, sorted(list(map(int, first_line))))
second_sorted_line = map(str, sorted(list(map(int, second_line))))
print(", ".join(first_sorted_line))
print(", ".join(second_sorted_line))

