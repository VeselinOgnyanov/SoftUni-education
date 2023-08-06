def shop_from_grocery_list(budget, *args):
    string_to_print = ""
    current_budget = budget
    shopping_list = list(args[0])
    prices = args[1:]
    for product, price in prices:
        if not shopping_list:
            break
        if product in shopping_list:
            if current_budget >= int(price):
                current_budget -= price
                shopping_list.remove(product)
            else:
                break
    if shopping_list:
        joined_list = ", ".join(shopping_list)
        string_to_print += f"You did not buy all the products. Missing products: {joined_list}."
        return string_to_print
    elif not shopping_list and current_budget >= 0:
        string_to_print += f"Shopping is successful. Remaining budget: {current_budget:.2f}."
        return string_to_print


