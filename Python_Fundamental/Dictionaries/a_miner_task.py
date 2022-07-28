command = input()
line_counter = 0
miner_dict = {}


while command != "stop":
    line_counter += 1
    if line_counter % 2 == 1:
        key = command
        if key not in miner_dict:
            miner_dict[key] = 0
    elif line_counter % 2 == 0:
        value = int(command)
        miner_dict[key] += value
    command = input()

for key, value in miner_dict.items():
    print(f"{key} -> {value}")