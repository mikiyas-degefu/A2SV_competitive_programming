# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_zero = defaultdict(int)
        col_zero = defaultdict(int)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_zero[i] = None
                    col_zero[j] = None

    
        for row in range(len(matrix)):
            if row in row_zero:
                matrix[row] = [0] * len(matrix[row])
            else:
                for col in range(len(matrix[row])):
                    if col in col_zero:
                        matrix[row][col] = 0

        


                
        
        


 




        