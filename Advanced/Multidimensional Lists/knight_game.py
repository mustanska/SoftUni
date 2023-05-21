from collections import deque


def knight_attack(field, positions):
    max_attack = 0
    max_coordinates = []

    for _ in range(len(positions)):
        position = positions.popleft()
        attack = 0
        for move in moves:
            current_row = position[0] + move[0]
            current_col = position[1] + move[1]

            if 0 <= current_row < size and 0 <= current_col < size:
                if field[current_row][current_col] == "K":
                    attack += 1

        if attack > max_attack:
            max_attack = attack
            max_coordinates = (position[0], position[1])

    return max_coordinates


def find_knights(field):
    position = deque()
    for i in range(size):
        for j in range(size):
            if field[i][j] == "K":
                position.append([i,j])
    return position


size = int(input())

board = [list(input()) for _ in range(size)]

knight_positions = find_knights(board)

moves = (
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
)

knights_attacked = 0

while True:
    attacked_knight_coordinates = knight_attack(board, knight_positions)

    if not attacked_knight_coordinates:
        break

    board[attacked_knight_coordinates[0]][attacked_knight_coordinates[1]] = "0"
    knights_attacked += 1
    knight_positions = find_knights(board)

print(knights_attacked)
