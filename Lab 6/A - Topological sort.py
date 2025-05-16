from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(order) == n:
    print(" ".join(map(str, order)))
else:
    print(-1)
