N = int(input())
x, y = map(int, input().split())

moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Top-left diagonal
    (-1, 1),  # Top-right diagonal
    (1, -1),  # Bottom-left diagonal
    (1, 1)    # Bottom-right diagonal
]

valid_moves = []

for dx, dy in moves:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        valid_moves.append((nx, ny))

valid_moves.sort()

print(len(valid_moves))
for move in valid_moves:
    print(move[0], move[1])