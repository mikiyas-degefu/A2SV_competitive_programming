# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        res = []

        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        for i in range(n):
            if safe[i]:
                res.append(i)
        
        return res