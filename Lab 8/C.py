import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v, i))

parent = list(range(n + 1))
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    pu, pv = find(u), find(v)
    if pu == pv:
        return False
    parent[pu] = pv
    return True

edges.sort()
in_mst = [False] * m
mst_cost = 0
adj = [[] for _ in range(n + 1)]

for w, u, v, i in edges:
    if union(u, v):
        in_mst[i] = True
        mst_cost += w
        adj[u].append((v, w))
        adj[v].append((u, w))

if sum(in_mst) != n - 1:
    print(-1)
    sys.exit()

LOG = 20
up = [[-1] * (n + 1) for _ in range(LOG)]
max_edge = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)

def dfs(u, p):
    for v, w in adj[u]:
        if v != p:
            depth[v] = depth[u] + 1
            up[0][v] = u
            max_edge[0][v] = w
            dfs(v, u)

dfs(1, -1)

for k in range(1, LOG):
    for v in range(1, n + 1):
        if up[k - 1][v] != -1:
            up[k][v] = up[k - 1][up[k - 1][v]]
            max_edge[k][v] = max(max_edge[k - 1][v], max_edge[k - 1][up[k - 1][v]])

def get_max_edge(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    res = 0
    for k in reversed(range(LOG)):
        if up[k][u] != -1 and depth[up[k][u]] >= depth[v]:
            res = max(res, max_edge[k][u])
            u = up[k][u]
    if u == v:
        return res
    for k in reversed(range(LOG)):
        if up[k][u] != -1 and up[k][u] != up[k][v]:
            res = max(res, max_edge[k][u], max_edge[k][v])
            u = up[k][u]
            v = up[k][v]
    return max(res, max_edge[0][u], max_edge[0][v])

second_best = float('inf')
for w, u, v, i in edges:
    if in_mst[i]:
        continue
    max_w = get_max_edge(u, v)
    if max_w != w:
        new_cost = mst_cost - max_w + w
        if new_cost > mst_cost:
            second_best = min(second_best, new_cost)

print(second_best if second_best != float('inf') else -1)
