def palindrome(current_string):
    straight_value = ""
    reversed_value = ""
    for index in range(len(current_string)):
        straight_value += current_string[index]
    for index in range(len(current_string) - 1, -1, -1):
        reversed_value += current_string[index]
    if straight_value == reversed_value:
        print("True")
    else:
        print("False")


some_string = input()
new_string_list = some_string.split(", ")
for element in new_string_list:
    palindrome(element)



