n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (n + 1)
adj_list = [[] for _ in range(n + 1)]

for i in range(m):
    degree[u[i]] += 1
    degree[v[i]] += 1
    adj_list[u[i]].append(v[i])
    adj_list[v[i]].append(u[i])
odd_count = 0
for d in degree:
    if d%2 !=0 :
        odd_count += 1

if odd_count != 0 and odd_count != 2:
    print("NO")
    exit()

visited = [False] * (n + 1)

start_node = -1
for i in range(1, n + 1):
    if degree[i] > 0:
        start_node = i
        break

if start_node == -1: 
    print("YES")
    exit()

stack = [start_node]
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                stack.append(neighbor)

for i in range(1, n + 1):
    if degree[i] > 0 and not visited[i]:
        print("NO")
        exit()

print("YES")
