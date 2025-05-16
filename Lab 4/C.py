n = int(input())

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    neighbors = data[1:]
    for j in neighbors:
        adj_matrix[i][j] = 1

for row in adj_matrix:
    print(" ".join(map(str, row)))