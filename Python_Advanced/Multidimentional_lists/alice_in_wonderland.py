def star_step():
    wonderland[alice_start_position[0]][alice_start_position[1]] = "*"
    return wonderland


def checking_tea_bags_quantity(tea_bags):
    if tea_bags >= 10:
        collected_flag = True
    else:
        collected_flag = False
    return collected_flag


def whether_symbol_is_r():
    if wonderland[next_step[0]][next_step[1]] == "R":
        wonderland[next_step[0]][next_step[1]] = "*"
        return wonderland


size = int(input())
wonderland = [input().split() for i in range(size)]
alice_start_position = []
tea_bag_quantity = 0
alice_current_position = []
tea_bags_are_collected = False


for row in range(len(wonderland)):
    if "A" in wonderland[row]:
        alice_start_position = [row, wonderland[row].index("A")]
        alice_current_position = alice_start_position
        break

star_step()

command = input()
while True:
    if command == "down":
        next_step = [alice_start_position[0] + 1, alice_start_position[1]]
        if next_step[0] >= size or wonderland[next_step[0]][next_step[1]] == "R":
            whether_symbol_is_r()
            break
        alice_current_position = wonderland[next_step[0]][next_step[1]]
        if alice_current_position.isdigit():
            tea_bag_quantity += int(alice_current_position)
        alice_start_position = next_step
        star_step()
        if checking_tea_bags_quantity(tea_bag_quantity):
            tea_bags_are_collected = True
            break

    elif command == "up":
        next_step = [alice_start_position[0] - 1, alice_start_position[1]]
        if next_step[0] < 0 or wonderland[next_step[0]][next_step[1]] == "R":
            whether_symbol_is_r()
            break
        alice_current_position = wonderland[next_step[0]][next_step[1]]
        if alice_current_position.isdigit():
            tea_bag_quantity += int(alice_current_position)
        alice_start_position = next_step
        star_step()
        if checking_tea_bags_quantity(tea_bag_quantity):
            tea_bags_are_collected = True
            break

    elif command == "left":
        next_step = [alice_start_position[0], alice_start_position[1] - 1]
        if next_step[1] < 0 or wonderland[next_step[0]][next_step[1]] == "R":
            whether_symbol_is_r()
            break
        alice_current_position = wonderland[next_step[0]][next_step[1]]
        if alice_current_position.isdigit():
            tea_bag_quantity += int(alice_current_position)
        alice_start_position = next_step
        star_step()
        if checking_tea_bags_quantity(tea_bag_quantity):
            tea_bags_are_collected = True
            break

    elif command == "right":
        next_step = [alice_start_position[0], alice_start_position[1] + 1]
        if next_step[0] >= size or wonderland[next_step[0]][next_step[1]] == "R":
            whether_symbol_is_r()
            break
        alice_current_position = wonderland[next_step[0]][next_step[1]]
        if alice_current_position.isdigit():
            tea_bag_quantity += int(alice_current_position)
        alice_start_position = next_step
        star_step()
        if checking_tea_bags_quantity(tea_bag_quantity):
            tea_bags_are_collected = True
            break

    command = input()

if tea_bags_are_collected:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for line in wonderland:
    print(" ".join(line))
