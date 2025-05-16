class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True

n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()  
dsu = DSU(n)

total_cost = 0
for w, u, v in edges:
    if dsu.union(u, v):
        total_cost += w

print(total_cost)
