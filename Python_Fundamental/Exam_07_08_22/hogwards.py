spell_to_be_deciphered = input()
new_spell = ""
command = input().split(" ")

while command[0] != "Abracadabra":
    if command[0] == "Abjuration":
        for element in spell_to_be_deciphered:
            new_spell += element.upper()
        spell_to_be_deciphered = new_spell
        print(spell_to_be_deciphered)
        new_spell = ""
    elif command[0] == "Necromancy":
        for element in spell_to_be_deciphered:
            new_spell += element.lower()
        spell_to_be_deciphered = new_spell
        print(spell_to_be_deciphered)
        new_spell = ""
    elif command[0] == "Illusion":
        if int(command[1]) > (len(spell_to_be_deciphered) - 1):
            print("The spell was too weak.")
        else:
            for index in range(len(spell_to_be_deciphered)):
                if index == int(command[1]):
                    new_spell += command[2]
                else:
                    new_spell += spell_to_be_deciphered[index]
            spell_to_be_deciphered = new_spell
            new_spell = ""
            print("Done!")
    elif command[0] == "Divination":
        if command[1] in spell_to_be_deciphered:
            new_spell = spell_to_be_deciphered.replace(command[1], command[2])
            spell_to_be_deciphered = new_spell
            print(spell_to_be_deciphered)
            new_spell = ""
        else:
            continue
    elif command[0] == "Alteration":
        if command[1] in spell_to_be_deciphered:
            new_spell = spell_to_be_deciphered.replace(command[1], "")
            spell_to_be_deciphered = new_spell
            print(spell_to_be_deciphered)
            new_spell = ""
        else:
            continue
    else:
        print("The spell did not work!")
    command = input().split(" ")



# test_string = "abcdefgh"
# new_string = test_string.replace("abc", "")
# print(new_string)