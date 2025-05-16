from collections import deque, defaultdict

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

n, m, s, d, k = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

path1 = bfs(graph, s, k)
if not path1:
    print(-1)
else:
    path2 = bfs(graph, k, d)
    if not path2:
        print(-1)
    else:
        full_path = path1 + path2[1:] 
        print(len(full_path) - 1)
        print(" ".join(map(str, full_path)))