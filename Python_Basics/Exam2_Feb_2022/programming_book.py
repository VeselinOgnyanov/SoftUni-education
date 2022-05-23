price_for_one_page = float(input())
price_for_one_cover = float(input())
percent_for_printing = int(input())
design_price = float(input())
crew_percent = int(input())

book_price = (price_for_one_page * 899) + (price_for_one_cover * 2)
perc_print = percent_for_printing / 100
book_price = book_price - book_price * perc_print
book_price += design_price
crew_percent = crew_percent / 100
crew_money = book_price * crew_percent
book_price = book_price - crew_money
money = book_price

print(f"Avtonom should pay {money:.2f} BGN.")