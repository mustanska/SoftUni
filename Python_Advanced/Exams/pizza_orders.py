from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacities = deque([int(x) for x in input().split(", ")])

total_pizzas = 0

while pizza_orders and employees_capacities:
    pizzas = pizza_orders.popleft()

    if pizzas <= 0 or pizzas > 10:
        continue

    employee_capacity = employees_capacities.pop()

    if pizzas <= employee_capacity:
        total_pizzas += pizzas

    else:
        total_pizzas += employee_capacity
        pizza_orders.appendleft(pizzas - employee_capacity)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(el) for el in employees_capacities])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizza_orders])}")