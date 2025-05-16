import heapq
from collections import defaultdict

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

def find_meeting_point(N, M, S, T, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist_from_s = dijkstra(graph, S, N)
    dist_from_t = dijkstra(graph, T, N)
    
    min_time = float('inf')
    meeting_node = -1
    for i in range(1, N + 1):
        max_time = max(dist_from_s[i], dist_from_t[i])
        if max_time < min_time:
            min_time = max_time
            meeting_node = i
        elif max_time == min_time and i < meeting_node:
            meeting_node = i
    
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time, meeting_node)

N, M, S, T = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

find_meeting_point(N, M, S, T, edges)