current_version = input().split(".")
final_list = []

new_version = "".join(current_version)
new_version = int(new_version)
new_version += 1
new_version = str(new_version)

for element in new_version:
    final_list.append(element)

final_list = ".".join(final_list)
print(final_list)