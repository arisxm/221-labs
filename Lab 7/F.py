import heapq
from collections import defaultdict

def second_shortest_path(N, M, S, D, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    pq = [(0, S, 0)] 
    dist = [[float('inf')] * 2 for _ in range(N + 1)]
    dist[S][0] = 0

    while pq:
        current_cost, node, path_count = heapq.heappop(pq)

        if path_count >= 2:
            continue

        for neighbor, weight in graph[node]:
            new_cost = current_cost + weight

            if new_cost < dist[neighbor][0]:
                dist[neighbor][1] = dist[neighbor][0]
                dist[neighbor][0] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, 0))

            elif dist[neighbor][0] < new_cost < dist[neighbor][1]:
                dist[neighbor][1] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, 1))

    return dist[D][1] if dist[D][1] != float('inf') else -1

N, M, S, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

result = second_shortest_path(N, M, S, D, edges)
print(result)