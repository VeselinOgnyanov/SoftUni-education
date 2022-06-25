def palindrome_string(current_string):
    test_string_forward = ""
    test_string_backward = ""
    palindrome = ""
    length = len(current_string)
    for forward_character in current_string:
        test_string_forward += forward_character
    for backward_character in range(length - 1, -1, -1):
        test_string_backward += current_string[backward_character]
    if test_string_forward == test_string_backward:
        palindrome = test_string_forward
        return palindrome


first_list = list(input().split())
palindrome_word = input()
palindrome_list = []
final_palindrome_list = []
palindrome_counter = 0
for element in first_list:
    if element == palindrome_word:
        palindrome_counter += 1
    palindrome_list.append(palindrome_string(element))
    final_palindrome_list = [x for x in palindrome_list if x != None]
print(final_palindrome_list)
print(f"Found palindrome {palindrome_counter} times")



