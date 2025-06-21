# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph) #map 0 color 1 and 1 color 2

        def dfs(node):
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = color[node] ^ 1 # 0 -> 1, 1 -> 0

                    if not dfs(nei):
                        return False
                
                elif color[node] == color[nei]:
                    return False

            
            return True

        
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
                    
        return True