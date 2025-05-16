import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

result = []
queue = [(0, N - 1)]

while queue:
    left, right = queue.pop(0)
    if left > right:
        continue
    mid = (left + right) // 2
    result.append(A[mid])
    queue.append((left, mid - 1))
    queue.append((mid + 1, right))

print(*result)
