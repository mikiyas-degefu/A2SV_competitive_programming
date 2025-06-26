# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        visited = set()
        i = 0

        for a,b in equations:
            val = values[i]
            graph[a].append((b,val)) 
            graph[b].append((a, 1/val))
            i += 1
        
        def dfs(cur, des, pdt, visited):
            #base case
            if cur == des:
                return pdt

            visited.add(cur)
            for nei, w in graph[cur]:
                if nei not in visited:
                    npdt = pdt * w
                    res = dfs(nei, des, npdt, visited)

                    if res != -1:
                        return res
            return -1
        res = []
        
        for a ,b in queries:
            if not a in graph or not b in graph:
                res.append(-1)
            else:
                qval = dfs(a, b, 1, set())
                res.append(qval)

        return res

        