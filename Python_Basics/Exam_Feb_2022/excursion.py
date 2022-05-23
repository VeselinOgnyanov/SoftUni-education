group_members = int(input())
number_nights = int(input())
transfer_cards = int(input())
museum_tickets = int(input())

price_nights = number_nights * 20
transfer_card_price = transfer_cards * 1.60
museum_ticket_price = museum_tickets * 6

sum_per_person = price_nights + transfer_card_price + museum_ticket_price
sum_per_group = sum_per_person * group_members

total_sum = sum_per_group * 1.25
print(f"{total_sum:.2f}")