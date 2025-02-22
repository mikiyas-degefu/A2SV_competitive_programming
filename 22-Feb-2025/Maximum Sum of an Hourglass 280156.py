# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = 0
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                sum_ = 0
                counter = 0
                
                #top elemenet 
                if i-1 >= 0:
                    sum_ += grid[i-1][j]
                    counter+=1
                #top left
                if i-1 >= 0 and j-1 >= 0:
                    sum_ += grid[i-1][j-1]
                    counter+=1
                #top right
                if i-1 >= 0 and j+1 < len(grid[i]):
                    sum_ += grid[i-1][j+1]
                    counter+=1
                #bottom
                if i+1 < len(grid):
                    sum_ += grid[i+1][j]
                    counter+=1
                #bottom left
                if i+1 < len(grid) and j-1 < len(grid[i]):
                    sum_ += grid[i+1][j-1]
                    counter+=1
                #top right
                if i+1 < len(grid) and j+1 < len(grid[i]):
                    sum_ += grid[i+1][j+1]
                    counter+=1
                
                if counter == 6:
                    sum_ += grid[i][j]
                    if sum_ > hourglass:
                        hourglass = sum_
        
        return hourglass




                    



        