import heapq
from collections import defaultdict

def find_min_cost_path(N, M, S, D, weights, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    pq = [(weights[S - 1], S)]
    dist = [float('inf')] * (N + 1)
    dist[S] = weights[S - 1]

    while pq:
        current_cost, node = heapq.heappop(pq)
        if current_cost > dist[node]:
            continue
        for neighbor in graph[node]:
            new_cost = current_cost + weights[neighbor - 1]
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return dist[D] if dist[D] != float('inf') else -1

N, M, S, D = map(int, input().split())
weights = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

result = find_min_cost_path(N, M, S, D, weights, edges)
print(result)