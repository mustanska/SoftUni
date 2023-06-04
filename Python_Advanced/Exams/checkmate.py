SIZE = 8

chess_board = []
king_position = []

for row in range(SIZE):
    chess_board.append(input().split())

    if "K" in chess_board[row]:
        king_position = [row, chess_board[row].index("K")]

positions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

is_safe = True

for row, col in positions:
    checked_row = row + king_position[0]
    checked_col = col + king_position[1]

    while 0 <= checked_row < SIZE and 0 <= checked_col < SIZE:
        if chess_board[checked_row][checked_col] == "Q":
            print([checked_row, checked_col])
            is_safe = False
            break

        checked_row += row
        checked_col += col

if is_safe:
    print("The king is safe!")