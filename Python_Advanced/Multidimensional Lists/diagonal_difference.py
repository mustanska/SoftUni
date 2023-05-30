n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
sum_primary = 0
sum_secondary = 0

for i in range(n):
    sum_primary += matrix[i][i]
    sum_secondary += matrix[i][n - i - 1]

print(abs(sum_primary - sum_secondary))