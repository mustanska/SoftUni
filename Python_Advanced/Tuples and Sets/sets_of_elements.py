m, n = input().split()

first_set = set(int(input()) for _ in range(int(m)))
second_set = set(int(input()) for _ in range(int(n)))

print(*first_set.intersection(second_set), sep="\n")
