SIZE = 8

chessboard = []
chessboard_positions = []
white_pos = []
black_pos = []

for rank in range(SIZE):
    chessboard.append(input().split())
    chessboard_positions.append([f"{chr(97 + col)}{SIZE - rank}" for col in range(SIZE)])

    if "w" in chessboard[rank]:
        white_pos.extend([rank, chessboard[rank].index("w")])

    elif "b" in chessboard[rank]:
        black_pos.extend([rank, chessboard[rank].index("b")])

if white_pos[1] - 1 == black_pos[1] or white_pos[1] + 1 == black_pos[1]:
    capture_rank = (white_pos[0] - black_pos[0]) // 2

    if (white_pos[0] - black_pos[0]) % 2 != 0:
        print(f"Game over! White win, capture on {chessboard_positions[black_pos[0] + capture_rank][black_pos[1]]}.")
    else:
        print(f"Game over! Black win, capture on {chessboard_positions[white_pos[0] - capture_rank][white_pos[1]]}.")

else:
    if SIZE - 1 - black_pos[0] < white_pos[0]:
        print(f"Game over! Black pawn is promoted to a queen at {chessboard_positions[SIZE - 1][black_pos[1]]}.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chessboard_positions[0][white_pos[1]]}.")