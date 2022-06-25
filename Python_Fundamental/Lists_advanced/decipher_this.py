ciphered_code = input().split()
integer_string = ""
word_string = ""
integer_list = []
word_list = []
char_list = []
final_list = []
for element in ciphered_code:
    for index in element:
        if index.isdigit():
            integer_string += str(index)
        else:
            word_string += str(index)
    integer_list.append(integer_string)
    word_list.append(word_string)
    integer_string = ""
    word_string = ""
reversed_list = []
for words in word_list:
    if len(words) >= 2:
        new_words = words[-1] + words[1:-1] + words[0]
        reversed_list.append(new_words)
    else:
        reversed_list.append(words)
for element in integer_list:
    char_list.append((chr(int(element))))
for number_index in range(len(char_list)):
    final_string = char_list[number_index] + reversed_list[number_index]
    final_list.append(final_string)

final_string = " ".join(final_list)

print(final_string)



