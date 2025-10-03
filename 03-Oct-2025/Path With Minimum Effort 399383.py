# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        minEffort = [[float('inf')] * cols for _ in range(rows)]
        minEffort[0][0] = 0
        
        heap = [(0, 0, 0)]
    
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    newEffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if newEffort < minEffort[nr][nc]:
                        minEffort[nr][nc] = newEffort
                        heapq.heappush(heap, (newEffort, nr, nc))
        
        return 0
