command = input()
products_price = {}
products_quantity = {}
final_product_price = {}
result = 0

while command != "buy":
    product_info = command.split(" ")
    if product_info[0] not in products_price:
        products_price[product_info[0]] = 0
    if product_info[0] not in products_quantity:
        products_quantity[product_info[0]] = 0
    products_price[product_info[0]] = float(product_info[1])
    products_quantity[product_info[0]] += int(product_info[2])
    command = input()

for key, value in products_price.items():
    final_product_price[key] = value * float(products_quantity[key])

for key, value in final_product_price.items():
    print(f"{key} -> {value:.2f}")
