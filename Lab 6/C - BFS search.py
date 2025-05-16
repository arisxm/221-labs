# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# x1, y1, x2, y2 = map(int, input().strip().split())

# x1 -= 1
# y1 -= 1
# x2 -= 1
# y2 -= 1

# if x1 == x2 and y1 == y2:
#     print(0)
#     exit()

# dx = [-2, -2, -1, -1, 1, 1, 2, 2]
# dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# visited = [[False] * n for _ in range(n)]
# visited[x1][y1] = True

# queue = deque()
# queue.append((x1, y1, 0))

# while queue:
#     x, y, d = queue.popleft()

#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             if nx == x2 and ny == y2:
#                 print(d + 1)
#                 exit()
#             else:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny, d + 1))

# print(-1)

import sys
from collections import deque

input = sys.stdin.read
data = input().split()

n = int(data[0])
x1, y1, x2, y2 = map(int, data[1:5])

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

if x1 == x2 and y1 == y2:
    print(0)
    sys.exit()

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

visited = [False] * (n * n)

def idx(x, y):
    return x * n + y

queue = deque()
queue.append((x1, y1, 0))
visited[idx(x1, y1)] = True

while queue:
    x, y, dist = queue.popleft()
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            i = idx(nx, ny)
            if not visited[i]:
                if nx == x2 and ny == y2:
                    print(dist + 1)
                    sys.exit()
                visited[i] = True
                queue.append((nx, ny, dist + 1))

print(-1)

