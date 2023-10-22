from collections import deque

# Входни данни
food_quantity = int(input())
orders = deque(map(int, input().split()))

# Променлива за най-голямата поръчка
largest_order = 0

# Намиране на най-голямата поръчка
for order in orders:
    if order > largest_order:
        largest_order = order

# Обслужване на клиентите
while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break

# Изходни данни
print(largest_order)

if not orders:
    print("Orders complete")
else:
    remaining_orders = ', '.join(map(str, orders))
    print(f"Оставащи поръчки: {remaining_orders}")
