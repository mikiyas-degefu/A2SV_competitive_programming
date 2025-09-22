# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, w in roads:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        visited = set()
        min_edge = float("inf")
        q = deque([1])
        
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for nei, w in graph[node]:
                min_edge = min(min_edge, w)
                if nei not in visited:
                    q.append(nei)
        
        return min_edge