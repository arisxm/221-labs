class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return self.size[xroot]
        
        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]
        return self.size[xroot]

n, k = map(int, input().split())
dsu = DSU(n)

for _ in range(k):
    a, b = map(int, input().split())
    print(dsu.union(a, b))
