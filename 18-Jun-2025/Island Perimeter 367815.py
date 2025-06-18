# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
                #top     #bot   #left   #right
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        self.total = 0
        visited = set()

        def is_valid(nr, nc):
            return 0 <= nr < len(grid) and 0 <= nc < len(grid[0])

        def dfs(row, col):
            visited.add((row, col))

            land = 4
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if is_valid(nr, nc) and  grid[nr][nc] == 1:
                    land -= 1
            self.total += land

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
        
        return self.total
        