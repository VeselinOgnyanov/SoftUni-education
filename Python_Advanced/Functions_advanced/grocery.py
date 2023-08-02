def grocery_store(**kwargs):
    sorted_groceries = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    grocery_string = ""
    for product, quantity in sorted_groceries:
        grocery_string += f"{product}: {quantity}\n"
    return grocery_string


print(grocery_store(bread=5, pasta=12, eggs=12, ))
print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1, ))
