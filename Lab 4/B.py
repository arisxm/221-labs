n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj_list = [[]for _ in range(n+1)]

for i in range(m):
    adj_list[u[i]].append((v[i],w[i]))

for node in range(1, n + 1):
    if adj_list[node]:
        edge_str = " ".join(f"({dest},{weight})" for dest, weight in adj_list[node])
        print(f"{node}: {edge_str}")
    else:
        print(f"{node}:")     