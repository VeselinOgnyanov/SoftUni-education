team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
team_a_is_less_than_seven = False
team_b_is_less_than_seven = False

cards = input()

quit_list = cards.split()
for index in range(len(quit_list)):
    if quit_list[index] in team_a:
        team_a.remove(quit_list[index])
        if len(team_a) < 7:
            team_a_is_less_than_seven = True
            break
    if quit_list[index] in team_b:
        team_b.remove(quit_list[index])
        if len(team_b) < 7:
            team_b_is_less_than_seven = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if team_a_is_less_than_seven or team_b_is_less_than_seven:
    print("Game was terminated")

