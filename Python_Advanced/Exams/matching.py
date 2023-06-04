from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    female = females.popleft()
    male = males.pop()

    if male <= 0:
        females.appendleft(female)
        continue

    if male % 25 == 0:
        males.pop()
        females.appendleft(female)
        continue

    if female <= 0:
        males.append(male)
        continue

    elif female % 25 == 0:
        females.popleft()
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")

print(f"Males left: {', '.join([str(el) for el in reversed(males)]) if males else 'none'}")
print(f"Females left: {', '.join([str(el) for el in females]) if females else 'none'}")
