def separate_string_to_letters(str_to_be_separated):
    separated_list = []
    for element in str_to_be_separated:
        separated_list.append(element)
    return separated_list


def remove_vowels(final_separated_list):
    last_string = ""
    has_vow = False
    vowels = ["a", "o", "u", "e", "i"]
    for element in separate_string_to_letters(final_separated_list):
        for vowel in vowels:
            if element == vowel:
                has_vow = True
                break
        if not has_vow:
            last_string += element
        has_vow = False
    print(last_string)


text = input()
remove_vowels(text)



