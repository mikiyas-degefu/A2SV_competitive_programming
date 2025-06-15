# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    neighbors = []
    for j in range(n):
        if adj_matrix[i][j] == 1:
            neighbors.append(j + 1)
    print(len(neighbors), *neighbors)
