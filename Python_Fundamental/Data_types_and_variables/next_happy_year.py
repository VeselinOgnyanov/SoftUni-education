start_year = int(input())
next_year = 0

while True:
    next_year = start_year + 1
    next_year = str(next_year)
    if next_year[0] != next_year[1] and next_year[0] != next_year[2] and next_year[0] != next_year[3]:
        if next_year[1] != next_year[2] and next_year[1] != next_year[3]:
            if next_year[2] != next_year[3]:
                next_year = int(next_year)
                break
    start_year += 1

print(next_year)
