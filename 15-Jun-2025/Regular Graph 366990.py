# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(int)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] += 1


degrees = [graph[i] for i in range(1, n + 1)]

if all(deg == degrees[0] for deg in degrees):
    print("YES")
else:
    print("NO")
