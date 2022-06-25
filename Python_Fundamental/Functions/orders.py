def total_price(product, quantity):
    if product == "coffee":
        price = 1.5
    elif product == "coke":
        price = 1.40
    if product == "water":
        price = 1.0
    if product == "snacks":
        price = 2.0
    final_func_price = quantity * price
    return final_func_price


selected_product = input()
selected_quantity = int(input())

final_price = total_price(selected_product, selected_quantity)
print(f"{final_price:.2f}")
