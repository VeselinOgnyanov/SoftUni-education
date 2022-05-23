import math

number_tournaments = int(input())
start_point = int(input())

final_point = start_point
wins = 0
finals = 0
semi_finals = 0

for i in range(number_tournaments):
    tournament_position = input()
    if tournament_position == "W":
        wins += 1
        final_point += 2000
    elif tournament_position == "F":
        finals += 1
        final_point += 1200
    else:
        semi_finals += 1
        final_point += 720
average_points = math.floor((final_point - start_point) / number_tournaments)
percent_wins = wins / number_tournaments * 100
print(f"Final points: {final_point}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")



