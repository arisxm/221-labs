N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append([0]*N)

for _ in range(M):
    u, v, w = map(int, input().split())
    matrix[u - 1][v - 1] = w

for row in matrix:
    print(' '.join(map(str, row)))