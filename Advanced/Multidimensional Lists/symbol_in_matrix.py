n = int(input())

matrix = [list(input()) for _ in range(n)]

special_symbol = input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == special_symbol:
            print((i, j))
            exit()

print(f"{special_symbol} does not occur in the matrix")