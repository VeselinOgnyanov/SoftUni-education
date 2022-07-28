deck_of_cards = input().split(", ")
number_of_commands = int(input())
length = len(deck_of_cards)
for _ in range(number_of_commands):
    command = input().split(", ")
    if command[0] == "Add":
        for elements in deck_of_cards:
            if command[1] in deck_of_cards:
                print("Card is already in the deck")
            else:
                deck_of_cards.append(command[1])
                print("Card successfully added")
            break
    elif command[0] == "Remove":
        if command[1] not in deck_of_cards:
            print("Card not found")
        else:
            deck_of_cards.remove(command[1])
            print("Card successfully removed")
    elif command[0] == "Remove At":
        if ((int(command[1])) < 0) or ((int(command[1])) > (length - 1)):
            print("Index out of range")
        else:
            deck_of_cards.pop(int(command[1]))
            print("Card successfully removed")
    elif command[0] == "Insert":
        if ((int(command[1])) < 0) or ((int(command[1])) > (length - 1)):
            print("Index out of range")
        else:
            if command[2] in deck_of_cards:
                print("Card is already added")
            else:
                deck_of_cards.insert(int(command[1]), command[2])
                print("Card successfully added")

print(", ".join(deck_of_cards))


