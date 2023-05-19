from collections import deque

rows, cols = [int(x) for x in input().split()]

string = list(input())

string_queue = deque(string)

for row in range(rows):
    while len(string_queue) < cols:
        string_queue.extend(string)

    if row % 2 == 0:
        print(*[string_queue.popleft() for _ in range(cols)], sep="")
    else:
        print(*[string_queue.popleft() for _ in range(cols)][::-1], sep="")

