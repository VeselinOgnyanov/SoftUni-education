data = input().split(" ")
bakery_dict = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    bakery_dict[key] = value

print(bakery_dict)