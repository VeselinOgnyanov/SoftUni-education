trip_price = float(input())
pieces_puzzles = int(input())
pieces_dolls = int(input())
pieces_bears = int(input())
pieces_minions = int(input())
pieces_trucks = int(input())

price_puzzles = 2.60
price_dolls = 3.0
price_bears = 4.10
price_minions = 8.20
price_trucks = 2.0
rent = 0

sum = (pieces_puzzles * price_puzzles ) + (pieces_dolls * price_dolls) \
      + (pieces_bears * price_bears) + (pieces_minions * price_minions) + (pieces_trucks * price_trucks)

if pieces_puzzles + pieces_bears + pieces_trucks + pieces_dolls \
    + pieces_minions >= 50:
    sum = sum * 0.75

rent = sum * 0.10
final_sum = sum - rent
money_left = final_sum - trip_price

if final_sum - trip_price >= 0:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = abs(money_left)
    print(f"Not enough money! {money_left:.2f} lv needed.")

