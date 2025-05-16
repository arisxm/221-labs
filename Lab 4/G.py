from math import gcd

N, Q = map(int, input().split())

neighbors = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if gcd(i, j) == 1:
            neighbors[i].append(j)
            neighbors[j].append(i)

for i in range(1, N + 1):
    neighbors[i].sort()

result = []
for idx in range(Q):
    X, K = map(int, input().split())

    if K > len(neighbors[X]) or K <= 0:
        result.append(-1)
    else:
        result.append(neighbors[X][K-1])

print("\n".join(map(str, result)))