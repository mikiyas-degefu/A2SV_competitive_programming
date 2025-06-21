# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        max_area = 0

        def in_bound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(r,c):
            area = 1
            visited.add((r,c))
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if in_bound(nr, nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    area += dfs(nr, nc)
            
            return area

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not (r,c) in visited and grid[r][c] == 1:
                   
                    max_area = max(max_area, dfs(r,c))
        
        return max_area

