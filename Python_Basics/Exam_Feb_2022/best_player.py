command = input()
current_player = ""
current_goals = 0
more_than_10_goals = False
while command != "END":
    number_goals = int(input())

    if current_goals < number_goals:
        current_goals = number_goals
        current_player = command
    if current_goals >= 10:
        more_than_10_goals = True
        break
    command = input()
if more_than_10_goals:
    print(f"{current_player} is the best player!")
    print(f"He has scored {current_goals} goals and made a hat-trick !!!")
else:
    print(f"{current_player} is the best player!")
    if current_goals >= 3:
        print(f"He has scored {current_goals} goals and made a hat-trick !!!")
    else:
        print(f"He has scored {current_goals} goals.")
