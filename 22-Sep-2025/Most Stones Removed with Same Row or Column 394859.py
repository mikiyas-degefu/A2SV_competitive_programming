# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = set()
        
        # adjacency list
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        stack.append(nei)
        
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return n - components