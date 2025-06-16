# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        N = len(edges)
        degree = defaultdict(int)

        for u,v in edges:
            degree[u] += 1
            degree[v] += 1

        for node, edges in degree.items():
            if edges == N:
                return node

        return -1
