lent = int(input())
width = int(input())
high = int(input())
percent_full = float(input())

volume = lent *  width * high
volume_water = volume / 1000
needed_percent = 1 - (percent_full / 100)
a = needed_percent
needed_litres = volume_water * needed_percent

print(needed_litres)