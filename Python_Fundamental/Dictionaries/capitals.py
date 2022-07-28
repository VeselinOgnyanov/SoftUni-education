counties = input().split(", ")
capitols = input().split(", ")

# new_dict = dict(zip(counties, capitols))
# for key, value in new_dict.items():
#     print(f"{key} -> {value}")

new_dict = {counties[index]: capitols[index] for index in range(len(counties))}
for key, value in new_dict.items():
    print(f"{key} -> {value}")

