from collections import deque

person_name = input()
customer_queue = deque([])

while True:
    if person_name == "Paid":
        for times in range(len(customer_queue)):
            new_element = customer_queue.popleft()
            print(new_element)
    elif person_name == "End":
        print(f"{len(customer_queue)} people remaining.")
        break
    else:
        customer_queue.append(person_name)
    person_name = input()
