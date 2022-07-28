command = input()
courses = {}

while command != "end":
    command = command.split(" : ")
    if command[0] not in courses:
        courses[command[0]] = []
    courses[command[0]].append(command[1])
    command = input()

for keys in courses.keys():
    print(f"{keys}: {len(courses[keys])}")
    for elements in courses[keys]:
        print(f"-- {elements}")