# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        
        queue = deque([(0, 0, health - grid[0][0])])
        
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = health - grid[0][0]
        
        while queue:
            x, y, h = queue.popleft()
            
            if (x, y) == (m-1, n-1) and h >= 1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_health = h - grid[nx][ny]
                    if new_health > 0 and new_health > visited[nx][ny]:
                        visited[nx][ny] = new_health
                        queue.append((nx, ny, new_health))
        
        return False
