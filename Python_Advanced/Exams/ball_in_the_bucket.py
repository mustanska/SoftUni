SIZE = 6
THROWS = 3

board = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(SIZE)]

presents = {
    "Football": lambda x: 100 <= x < 200,
    "Teddy Bear": lambda x: 200 <= x < 300,
    "Lego Construction Set": lambda x: x >= 300,
}

score = 0

for _ in range(THROWS):
    current_row, current_col = [int(x) for x in input()[1:-1].split(", ")]

    if not (0 <= current_row < SIZE and 0 <= current_col < SIZE):
        continue

    if board[current_row][current_col] == "B":
        board[current_row][current_col] = 0

        score += sum([board[row][current_col] for row in range(SIZE)])

for present, value in presents.items():
    if value(score):
        print(f"Good job! You scored {score} points, and you've won {present}.")
        break
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")