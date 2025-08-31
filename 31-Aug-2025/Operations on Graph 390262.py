# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict

def is_regular(graph: dict) -> bool:
    # Extract degrees of all vertices
    degrees = [len(neighbors) for neighbors in graph.values()]
    if not degrees:  # Handle empty graph
        return True
    first_degree = degrees[0]
    return all(degree == first_degree for degree in degrees)

# Input: n = number of vertices, m = number of edges
n, m = map(int, input().split())
graph = defaultdict(list)

# Initialize vertices (in case some are isolated)
for v in range(1, n + 1):
    graph[v] = []

# Read edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Check regularity
print("YES" if is_regular(graph) else "NO")