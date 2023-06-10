from collections import deque

SIZE_OF_BOX = 50

eggs = deque([int(x) for x in input().split(", ")])
pieces_of_paper = deque([int(x) for x in input().split(", ")])

total_boxes = 0

while eggs and pieces_of_paper:
    egg = eggs.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue

    piece_of_paper = pieces_of_paper.pop()

    wrapped_egg = egg + piece_of_paper

    if wrapped_egg <= SIZE_OF_BOX:
        total_boxes += 1


if total_boxes:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(el) for el in eggs])}")

if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join([str(el) for el in pieces_of_paper])}")