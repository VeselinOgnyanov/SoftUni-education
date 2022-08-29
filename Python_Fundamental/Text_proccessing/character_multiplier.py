text = input().split(" ")
smallest_string = ""
biggest_string = ""
first_string = text[0]
second_string = text[1]
multiplied_result = 0

if len(first_string) > len(second_string):
    smallest_string = second_string
    biggest_string = first_string
else:
    smallest_string = first_string
    biggest_string = second_string

for index in range(len(smallest_string)):
    multiplied_result += (ord(first_string[index]) * ord(second_string[index]))

if len(first_string) != len(second_string):
    additional_value = 0
    for index in range(len(smallest_string), len(biggest_string)):
        additional_value += ord(biggest_string[index])
    multiplied_result += additional_value

print(multiplied_result)