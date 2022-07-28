command = input()
product_dict = {}

while command != "statistics":
    product = command.split(": ")
    key = product[0]
    value = int(product[1])
    if key not in product_dict:
        product_dict[key] = int(value)
    else:
        product_dict[key] += value

    command = input()
print("Products in stock:")

for key, value in product_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(product_dict)}")
print(f"Total Quantity: {sum(product_dict.values())}")
