list_of_strings = input().split(" ")
# print(list_of_strings)
result = ""
for elements in list_of_strings:
    current_length = len(elements)
    result += elements * current_length

print(result)