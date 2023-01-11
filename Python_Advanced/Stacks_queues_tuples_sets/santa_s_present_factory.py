from collections import deque

materials_for_crafting = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

while materials_for_crafting and magic_level:
