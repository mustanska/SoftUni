elements = set()

for _ in range(int(input())):
    line = input().split()

    for element in line:
        elements.add(element)

print(*elements, sep="\n")