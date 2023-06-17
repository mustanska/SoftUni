from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = [int(x) for x in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        if substance - 1 > 0:
            substances.append(substance - 1)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(el) for el in tools])}")
if substances:
    print(f"Substances: {', '.join([str(el) for el in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(el) for el in challenges])}")