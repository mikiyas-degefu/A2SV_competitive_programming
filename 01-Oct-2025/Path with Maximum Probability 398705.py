# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        

        pq = [(-1.0, start_node)]  
        best = [0.0] * n
        best[start_node] = 1.0

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  

            if node == end_node:
                return prob  

            for nei, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > best[nei]:
                    best[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))
        
        return 0.0
