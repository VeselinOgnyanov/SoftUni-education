tools = list(map(int, input().split()))
substances = list(map(int, input().split()))
substances.reverse()
challenges = list(map(int, input().split()))
harry_is_lost = False
while challenges:
    result = tools[0] * substances[0]
    if result in challenges:
        tools.pop(0)
        substances.pop(0)
        challenges.remove(result)
    else:
        tools[0] = tools[0] + 1
        buffer = tools.pop(0)
        tools.append(buffer)
        substances[0] = substances[0] - 1
        if substances[0] <= 0:
            substances.pop(0)

    if (not len(tools) or not len(substances)) and challenges:
        harry_is_lost = True
        break
    elif not challenges:
        break

joined_tools = list(map(str, tools))
joined_tools = ", ".join(joined_tools)
joined_substances = list(map(str, substances))
joined_substances.reverse()
joined_substances = ", ".join(joined_substances)
joined_challenges = list(map(str, challenges))
joined_challenges = ", ".join(joined_challenges)

if harry_is_lost:
    print("Harry is lost in the temple. Oblivion awaits him.")
    if tools:
        print(f"Tools: {joined_tools}")
    if substances:
        print(f"Substances: {joined_substances}")
    if challenges:
        print(f"Challenges: {joined_challenges}")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {joined_tools}")
    if substances:
        print(f"Substances: {joined_substances}")
    if challenges:
        print(f"Challenges: {joined_challenges}")
