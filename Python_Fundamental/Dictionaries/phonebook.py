text = input()
phonebook = {}

while "-" in text:
    current_contact_list = text.split("-")
    key = current_contact_list[0]
    value = current_contact_list[1]
    if key not in phonebook:
        phonebook[key] = ""
    phonebook[key] = value
    text = input()

number_of_counts = int(text)
for _ in range(number_of_counts):
    searched_contact = input()
    if searched_contact in phonebook:
        print(f"{searched_contact} -> {phonebook[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")



