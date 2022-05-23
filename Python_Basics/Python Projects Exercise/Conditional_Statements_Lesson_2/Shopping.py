budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

discount = 0

video_card_price = number_video_cards * 250
processor_price = (video_card_price * 0.35) * number_processors
ram_price = (video_card_price * 0.10) * number_ram

total_price = video_card_price + processor_price + ram_price

if number_video_cards > number_processors:
    discount = total_price * 0.15
    total_price -= discount
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")