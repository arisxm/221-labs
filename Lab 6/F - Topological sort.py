from collections import defaultdict, deque

n = int(input())
words = [input().strip() for _ in range(n)]

graph = defaultdict(set)
indegree = defaultdict(int)
all_chars = set("".join(words))

invalid = False
for i in range(n - 1):
    w1 = words[i]
    w2 = words[i + 1]
    min_len = min(len(w1), len(w2))
    if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
        invalid = True
        break
    for j in range(min_len):
        if w1[j] != w2[j]:
            if w2[j] not in graph[w1[j]]:
                graph[w1[j]].add(w2[j])
                indegree[w2[j]] += 1
            break

if invalid:
    print(-1)
else:

    zero_indegree = [c for c in all_chars if indegree[c] == 0]
    zero_indegree.sort()

    result = []
    while zero_indegree:
        c = zero_indegree.pop(0)
        result.append(c)
        for nei in sorted(graph[c]):
            indegree[nei] -= 1
            if indegree[nei] == 0:
                zero_indegree.append(nei)
        zero_indegree.sort()

    if len(result) != len(all_chars):
        print(-1)
    else:
        print("".join(result))
