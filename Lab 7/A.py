import heapq
from collections import defaultdict, deque

def shortest_path(N, M, S, D, u, v, w):
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))

    dist = [float('inf')] * (N + 1)
    parent = [-1] * (N + 1)
    dist[S] = 0
    pq = [(0, S)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                parent[neighbor] = node
                heapq.heappush(pq, (dist[neighbor], neighbor))

    if dist[D] == float('inf'):
        print(-1)
        return

    path = deque()
    current = D
    while current != -1:
        path.appendleft(current)
        current = parent[current]

    print(dist[D])
    print(*path)

N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

shortest_path(N, M, S, D, u, v, w)