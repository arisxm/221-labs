import heapq
from collections import defaultdict

def find_min_distance_with_parity(N, M, u, v, w):
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))

    pq = [(0, 1, -1)]  
    dist = [[float('inf')] * 2 for _ in range(N + 1)] 
    dist[1][0] = dist[1][1] = 0

    while pq:
        current_cost, node, last_parity = heapq.heappop(pq)
        for neighbor, weight in graph[node]:
            current_parity = weight % 2
            if current_parity != last_parity:
                new_cost = current_cost + weight
                if new_cost < dist[neighbor][current_parity]:
                    dist[neighbor][current_parity] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, current_parity))

    result = min(dist[N])
    return result if result != float('inf') else -1

N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

result = find_min_distance_with_parity(N, M, u, v, w)
print(result)