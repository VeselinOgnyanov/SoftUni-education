data = input().split(" ")
searched_products = input().split(" ")
my_dict = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    my_dict[key] = value

for element in searched_products:
    if element in my_dict:
        print(f"We have {my_dict[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")


