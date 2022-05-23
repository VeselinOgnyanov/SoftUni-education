command = input()
total_coffee = 0
coffee_exceeded = False
while command != "END":
    if command == "coding":
        total_coffee += 1
    elif command == "CODING":
        total_coffee += 2
    if command == "dog" or command == "cat":
        total_coffee += 1
    elif command == "DOG" or command == "CAT":
        total_coffee += 2
    if command == "movie":
        total_coffee += 1
    elif command == "MOVIE":
        total_coffee += 2
    if total_coffee > 5:
        coffee_exceeded = True
        break
    else:
        command = input()
        continue
if coffee_exceeded:
    print("You need extra sleep")
else:
    print(total_coffee)

