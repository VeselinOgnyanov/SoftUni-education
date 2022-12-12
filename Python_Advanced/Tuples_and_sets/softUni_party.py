number_of_guests = int(input())
clients = set()
guests = set()
for _ in range(number_of_guests):
    current_client = input()
    clients.add(current_client)

command = input()
while command != "END":
    guests.add(command)
    command = input()

difference_set = clients - guests
sorted_set = sorted(difference_set)
print(len(sorted_set))
for el in sorted_set:
    print(el)
