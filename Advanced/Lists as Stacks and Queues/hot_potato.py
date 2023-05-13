from collections import deque
children = deque(input().split())

number_to_leave = int(input())

while len(children) != 1:
    children.rotate(-number_to_leave + 1)
    print(f"Removed {children.popleft()}")

print(f"Last is {children[-1]}")
