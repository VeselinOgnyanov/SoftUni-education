command = input()
voldemort_is_summoned = False
while command != "Welcome!":
    length = len(command)
    if command == "Voldemort":
        voldemort_is_summoned = True
        break
    elif length < 5:
        print(f"{command} goes to Gryffindor.")
    elif length == 5:
        print(f"{command} goes to Slytherin.")
    elif length == 6:
        print(f"{command} goes to Ravenclaw.")
    elif length > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if voldemort_is_summoned:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")

