# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]

edges = set()

for i in range(n):
    for j in range(i + 1, n):
        if mat[i][j] == 1:
            edges.add((i, j))

print(len(edges))
