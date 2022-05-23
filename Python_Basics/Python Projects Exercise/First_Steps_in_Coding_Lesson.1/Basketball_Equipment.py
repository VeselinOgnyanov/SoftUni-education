year_price = int(input())

basket_shoes = year_price * 0.60
basket_clothes = basket_shoes * 0.80
basket_ball = basket_clothes * 0.25
basket_acces = basket_ball * 0.20

price = year_price + basket_shoes + basket_clothes + basket_ball + basket_acces

print(price)