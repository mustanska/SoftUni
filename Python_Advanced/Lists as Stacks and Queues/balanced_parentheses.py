from collections import deque

parentheses = input()
open_parentheses = deque()

for parenthese in parentheses:
    if parenthese in "([{":
        open_parentheses.append(parenthese)
        continue

    if not open_parentheses:
        print("NO")
        break

    last_open = open_parentheses.pop()

    if last_open + parenthese not in "(){}[]":
        print("NO")
        break
else:
    print("YES")