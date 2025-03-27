# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefix = [[0] * (col + 1) for c in range(row + 1)]

        for i in range(row):
            prefix = 0
            for j in range(col):
                prefix+=matrix[i][j]
                above = self.prefix[i][j + 1] 
                self.prefix[i + 1][j + 1] = prefix + above
        print(self.prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1

        bottom_right = self.prefix[row2][col2]
        top_left = self.prefix[row1 - 1][col1 - 1]
        
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        

        return bottom_right - above - left + top_left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)