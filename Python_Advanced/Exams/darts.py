SIZE = 7
SCORE = 501


def player_hit(row, col):
    if not (0 <= row < SIZE and 0 <= col < SIZE):
        return 0

    if isinstance(dartboard[row][col], int):
        return dartboard[row][col]

    if dartboard[row][col] == "D":
        return sum_numbers_in_directions(row, col) * 2

    if dartboard[row][col] == "T":
        return sum_numbers_in_directions(row, col) * 3

    if dartboard[row][col] == "B":
        return SCORE


def sum_numbers_in_directions(row, col):
    sum_numbers = 0

    for move_row, move_col in moves:
        current_row = move_row + row
        current_col = move_col + col
        while not isinstance(dartboard[current_row][current_col], int):
            current_row += move_row
            current_col += move_col

        sum_numbers += dartboard[current_row][current_col]

    return sum_numbers


players = input().split(", ")

dartboard = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(SIZE)]

first_player_score = SCORE
second_player_score = SCORE
first_player_turns = 0
second_player_turns = 0

moves = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

while True:
    first_player_row, first_player_col = [int(x) for x in input()[1:-1].split(", ")]
    first_player_turns += 1
    first_player_score -= player_hit(first_player_row, first_player_col)

    if first_player_score <= 0:
        print(f"{players[0]} won the game with {first_player_turns} throws!")
        break

    second_player_row, second_player_col = [int(x) for x in input()[1:-1].split(", ")]
    second_player_turns += 1
    second_player_score -= player_hit(second_player_row, second_player_col)

    if second_player_score <= 0:
        print(f"{players[1]} won the game with {second_player_turns} throws!")
        break
