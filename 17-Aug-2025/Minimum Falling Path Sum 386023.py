# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #iterate all first col
        #row,col -> 
        #   row + 1, col - 1
        #   row + 1, col
        #   row + 1, col + 1

        memp = {}

        dirs = [(1,-1), (1, 0), (1,1)]

        def inbound(r,c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

        def dp(r,c):
            if r == len(matrix) - 1:
                return matrix[r][c]
            
            if (r, c) in memp:
                return memp[(r, c)]

            min_sum = float('inf')

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if inbound(nr, nc):
                    min_sum = min(min_sum, dp(nr, nc))
            
            memp[(r, c)] = matrix[r][c] + min_sum
            return memp[(r, c)]
        

        min_sum = float('inf')

        for i in range(len(matrix[0])):
            min_sum = min(min_sum, dp(0,i))
        
        return min_sum
        