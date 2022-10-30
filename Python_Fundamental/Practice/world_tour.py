all_stops = input()
command = input()
new_stop = ""
while True:
    if command == "Travel":
        break
    else:
        command = command.split(":")
        if command[0] == "Add Stop":
            if int(command[1]) <= (len(all_stops) - 1) and (int(command[1]) >= 0):
                new_stop = all_stops[0:int(command[1])] + str(command[2]) +\
                           all_stops[int(command[1]):len(all_stops) + 1]
                all_stops = new_stop
                print(all_stops)
            else:
                print(all_stops)
                command = input()
                continue
        elif command[0] == "Remove Stop":
            if int(command[1]) >= 0 and (int(command[1]) <= len(all_stops)):
                new_stop = all_stops[0:int(command[1])] + all_stops[int(command[2]) + 1:len(all_stops) + 1]
                all_stops = new_stop
                print(all_stops)
            else:
                print(all_stops)
                command = input()
                continue
        else:           # for command == "Switch"
            if command[1] in all_stops:
                new_stop = all_stops.replace(command[1], command[2])
                all_stops = new_stop
                print(all_stops)
            else:
                print(all_stops)
                command = input()
                continue
        command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")