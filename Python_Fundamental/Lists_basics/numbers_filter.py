quantity_of_integers = int(input())

even_integer_list = []
odd_integer_list = []
positive_integer_list = []
negative_integer_list = []

for _ in range(quantity_of_integers):
    current_integer = int(input())
    if current_integer == 0 or current_integer % 2 == 0:
        even_integer_list.append(current_integer)
    if current_integer % 2 == 1:
        odd_integer_list.append(current_integer)
    if current_integer == 0 or current_integer > 0:
        positive_integer_list.append(current_integer)
    if current_integer < 0:
        negative_integer_list.append(current_integer)

command = input()

if command == "even":
    print(even_integer_list)
if command == "odd":
    print(odd_integer_list)
if command == "negative":
    print(negative_integer_list)
if command == "positive":
    print(positive_integer_list)