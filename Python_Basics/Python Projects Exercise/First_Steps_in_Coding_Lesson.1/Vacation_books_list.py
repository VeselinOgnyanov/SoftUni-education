import math

number_of_pages = int(input())
pages_per_hour = int(input())
days_needed = int(input())

common_time_for_book = number_of_pages / pages_per_hour
needed_hours_per_day = common_time_for_book / days_needed

print(math.floor(needed_hours_per_day))
