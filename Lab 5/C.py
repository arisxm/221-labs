from collections import deque, defaultdict

def find_shortest_path(N, M, S, D, u, v):
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append(v[i])
        graph[v[i]].append(u[i])

    for key in graph:
        graph[key].sort()

    queue = deque([(S, [S])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if current == D:
            print(len(path) - 1)
            print(" ".join(map(str, path)))
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    print(-1)

N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
find_shortest_path(N, M, S, D, u, v)