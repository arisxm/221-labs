import sys
sys.setrecursionlimit(2 * 10**5 + 5)

def dfs(u, adj, visited, result):
    visited[u] = True
    result.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited, result)

N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
for i in range(M):
    adj[u[i]].append(v[i])
    adj[v[i]].append(u[i])

for i in range(1, N + 1):
    adj[i].sort()

visited = [False] * (N + 1)
result = []
dfs(1, adj, visited, result)

print(" ".join(map(str, result)))