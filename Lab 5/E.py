def has_cycle(n, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    state = [0] * (n + 1)

    def dfs_iterative(start):
        stack = [(start, 0)]
        path = []

        while stack:
            node, i = stack[-1]

            if state[node] == 0:
                state[node] = 1
                path.append(node)
            elif state[node] == 2:
                stack.pop()
                if path and path[-1] == node:
                    path.pop()
                continue
            elif state[node] == 1 and i == len(graph[node]):
                state[node] = 2
                stack.pop()
                if path and path[-1] == node:
                    path.pop()
                continue

            if i < len(graph[node]):
                neighbor = graph[node][i]
                stack[-1] = (node, i + 1)

                if state[neighbor] == 0:
                    stack.append((neighbor, 0))
                elif state[neighbor] == 1:
                    return True
            else:
                state[node] = 2
                stack.pop()
                if path and path[-1] == node:
                    path.pop()

        return False


    for node in range(1, n + 1):
        if state[node] == 0:
            if dfs_iterative(node):
                return "YES"
    return "NO"


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(has_cycle(n, edges))
