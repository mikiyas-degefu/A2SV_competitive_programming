# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        self.land = 0
        visited = set()

        def in_bound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            visited.add((r,c))

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if in_bound(nr, nc) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                    dfs(nr, nc)
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    self.land += 1
                    
                    
    
        return self.land
        
