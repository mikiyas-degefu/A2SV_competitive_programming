# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = 0

        rows, cols = len(grid), len(grid[0])
        fresh = 0  # Count fresh oranges

        # Find all initial rotten oranges and count fresh ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
                    minutes = time + 1  

        return minutes if fresh == 0 else -1

        