import sys
sys.setrecursionlimit(2 * 10**5 + 5)
input = sys.stdin.readline

N, R = map(int, input().strip().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

subtree_size = [0] * (N + 1)

def dfs(node, parent):
    subtree_size[node] = 1  
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]
        continue

dfs(R, -1)

Q = int(input())
for _ in range(Q):
    X = int(input())
    print(subtree_size[X])
