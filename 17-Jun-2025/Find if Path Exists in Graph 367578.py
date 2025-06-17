# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(cur):
            if cur == destination:
                return True

            if cur in visited:
                return False
            
            visited.add(cur)
            for neighbor in graph[cur]:
                if dfs(neighbor):
                    return True
            
            return False
        
        return dfs(source)
        



        