# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary, secondary = 0,0
        mid = 0
        for i in range(len(mat)):
            if i == len(mat) // 2:
                mid = mat[i][i]
            primary += mat[i][i]
            secondary += mat[i][len(mat) -1  - i]
        
        if len(mat) % 2:
            return primary + secondary - mid
        
        return primary + secondary

        