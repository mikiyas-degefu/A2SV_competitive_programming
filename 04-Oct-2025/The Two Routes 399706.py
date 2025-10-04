# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in range(1, n+1):
            if graph[u][v] and dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

n, m = map(int, input().split())
railway = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    railway[u][v] = railway[v][u] = 1

road = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j and not railway[i][j]:
            road[i][j] = 1

train_dist = bfs(1, railway, n)
bus_dist = bfs(1, road, n)

if train_dist[n] == -1 or bus_dist[n] == -1:
    print(-1)
else:
    print(max(train_dist[n], bus_dist[n]))