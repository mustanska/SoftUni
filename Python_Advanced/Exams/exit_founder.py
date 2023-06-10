from collections import deque

SIZE = 6

players = deque(input().split(", "))

maze_board = [input().split() for _ in range(SIZE)]

hit_the_wall = {players[0]: False, players[1]: False}

while True:
    row, col = [int(x) for x in input()[1:-1].split(", ")]

    if hit_the_wall[players[0]]:
        hit_the_wall[players[0]] = False
        players.rotate()
        continue

    if maze_board[row][col] == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break

    elif maze_board[row][col] == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    elif maze_board[row][col] == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        hit_the_wall[players[0]] = True

    players.rotate()
