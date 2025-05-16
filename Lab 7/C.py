import heapq
from collections import defaultdict

def minimize_danger(N, M, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    pq = [(0, 1)]
    danger = [float('inf')] * (N + 1)
    danger[1] = 0

    while pq:
        max_danger, city = heapq.heappop(pq)
        if max_danger > danger[city]:
            continue
        for neighbor, weight in graph[city]:
            new_danger = max(max_danger, weight)
            if new_danger < danger[neighbor]:
                danger[neighbor] = new_danger
                heapq.heappush(pq, (new_danger, neighbor))

    result = [danger[i] if danger[i] != float('inf') else -1 for i in range(1, N + 1)]
    return result

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

result = minimize_danger(N, M, edges)
print(*result)