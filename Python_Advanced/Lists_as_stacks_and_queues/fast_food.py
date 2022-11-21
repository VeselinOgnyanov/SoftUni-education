from collections import deque


quantity_of_food = int(input())
que_of_orders = map(int, input().split())
deque_of_orders = deque(que_of_orders)
max_order = max(deque_of_orders)
buffer_que = deque_of_orders.copy()
orders_not_completed = False
print(max_order)

for _ in range(len(deque_of_orders)):
    if quantity_of_food - buffer_que.popleft() < 0:
        print("Orders left: ", end="")
        for _ in range(len(deque_of_orders)):
            print(deque_of_orders.popleft(), end=" ")
        orders_not_completed = True
        break
    else:
        quantity_of_food -= deque_of_orders.popleft()

if not orders_not_completed:
    print("Orders complete")


