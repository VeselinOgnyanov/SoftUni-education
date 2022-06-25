number_of_electrons = int(input())

electrons_left = number_of_electrons
electron_distribution_list = []
for number in range(1, number_of_electrons):
    current_shell_capacity = 2*(number ** 2)
    if electrons_left >= current_shell_capacity:
        electron_distribution_list.append(current_shell_capacity)
        electrons_left -= current_shell_capacity
        continue
    elif electrons_left == 0:
        break
    else:
        electron_distribution_list.append(electrons_left)
        break

print(electron_distribution_list)