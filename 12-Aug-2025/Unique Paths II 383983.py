# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        C = len(obstacleGrid[0])
       
        path = [(1,0), (0,1)]

        memo = {}

        def in_bound(i,j):
            return 0 <= i < N and 0 <= j < C

        def dp(r,c):
            value = 0
            if obstacleGrid[r][c] == 1:
                return 0

            if r == N-1 and c == C-1:
                return 1
            
            if (r,c) in memo:
                return memo[(r,c)]

            for dr, dc in path:
                nr = dr + r
                nc = dc + c

                if in_bound(nr, nc) and obstacleGrid[nr][nc] != 1:
                    value += dp(nr, nc)
            
            
            memo[(r,c)] = value
            return value

        return dp(0,0)
        