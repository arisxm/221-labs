from collections import deque

def max_diamonds(rows, cols, grid):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_row, start_col):
        queue = deque()
        queue.append((start_row, start_col))
        visited[start_row][start_col] = True

        diamonds = 0
        if grid[start_row][start_col] == 'D':
            diamonds += 1

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if not visited[new_row][new_col] and grid[new_row][new_col] != '#':
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))
                        if grid[new_row][new_col] == 'D':
                            diamonds += 1

        return diamonds

    max_diamond_count = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c] and grid[r][c] != '#':
                current_count = bfs(r, c)
                if current_count > max_diamond_count:
                    max_diamond_count = current_count

    return max_diamond_count

r, h = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(input().strip())
print(max_diamonds(r, h, grid))
