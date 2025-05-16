import sys
sys.setrecursionlimit(2 * 10**5 + 5)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(node, parent, depth):
    farthest = (depth, node)
    for neighbor in tree[node]:
        if neighbor != parent:
            candidate = dfs(neighbor, node, depth + 1)
            if candidate[0] >= farthest[0]:
                farthest = candidate
    return farthest

x, u = dfs(1, -1, 0)

y, v = dfs(u, -1, 0)

print(y)
print(u, v)
