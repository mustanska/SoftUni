from collections import deque
queue = deque()

while True:
    name = input()

    if name == "End":
        print(f"{len(queue)} people remaining.")
        break

    if name == "Paid":
        while queue:
            print(queue.popleft())
        continue

    queue.append(name)
