pens = 5.80
markers = 7.20
dash_cleaner = 1.20

needed_pens = int(input())
needed_markers = int(input())
litres_dash_cleaner = int(input())
discount = int(input())

discount = float(discount/100)

price_pens = needed_pens * pens
price_markers = needed_markers * markers
price_dash_cleaner = dash_cleaner * litres_dash_cleaner
total_price = price_pens + price_markers + price_dash_cleaner
total_discount_price = total_price - (total_price * discount)

print(total_discount_price)

