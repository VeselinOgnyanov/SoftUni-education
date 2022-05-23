type_movie = input()
rows = int(input())
columns = int(input())

number_seats = rows * columns
total_price = 0
if type_movie == "Premiere":
    total_price = number_seats * 12.0
elif type_movie == "Normal":
    total_price = number_seats * 7.50
else:
    total_price = number_seats * 5.0
print(f"{total_price:.2f}")

