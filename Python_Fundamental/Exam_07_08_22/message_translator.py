import re

number_of_messages = int(input())
pattern = r"(!\b[A-Z][a-z]{3,}\b!):(\[[A-za-z]{8,}\])"
all_ascii_values = []
extracted_ascii_value = ""

for _ in range(number_of_messages):
    secret_message = input()
    valid_messages = re.search(pattern, secret_message)
    if valid_messages:
        new_list_group = [x for x in valid_messages.groups()]
        first_element = new_list_group[0]
        first_element = first_element.replace("!", "")
        second_element = new_list_group[1]
        second_element = second_element.replace("[", "")
        second_element = second_element.replace("]", "")
        for element in second_element:
            current_ascii_value = ord(element)
            all_ascii_values.append(str(current_ascii_value))
            extracted_ascii_value = " ".join(all_ascii_values)
        print(f"{first_element}: {extracted_ascii_value}")
        all_ascii_values = []
        extracted_ascii_value = ""
    else:
        print("The message is invalid")

