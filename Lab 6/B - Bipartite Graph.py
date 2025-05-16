from collections import deque, defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n+1)
max_group_size = 0

for i in range(1, n + 1):
    if visited[i] == -1:
        queue = deque()
        queue.append(i)
        visited[i] = 0  
        count = [1, 0] 

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1 - visited[node]
                    count[visited[neighbor]] += 1
                    queue.append(neighbor)
                elif visited[neighbor] == visited[node]:
                    
                    continue

        max_group_size += max(count)

print(max_group_size)