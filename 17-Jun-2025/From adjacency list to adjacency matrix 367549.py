# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    relation = list(map(int, input().split()))

    for v in relation[1:]:
        graph[i][v-1] = 1

for row in graph:
    print(*row)