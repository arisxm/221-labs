from collections import deque

def bfs_traversal(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    for neighbors in graph:
        neighbors.sort()
    
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

result = bfs_traversal(n, edges)
print(" ".join(map(str, result)))