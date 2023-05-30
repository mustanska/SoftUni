numbers = [x.split() for x in input().split("|") if x.split()]

[print(*row, end=" ") for row in numbers[::-1]]