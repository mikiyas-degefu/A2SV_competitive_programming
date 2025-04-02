# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        max_sqare = 0
        min_sqare = 0
        while (max_sqare * max_sqare) < c:
            max_sqare+=1
        
        while min_sqare <= max_sqare:
            result = pow(min_sqare, 2) + pow(max_sqare, 2)
            if result == c:
                return True
            elif result > c:
                max_sqare -= 1
            else:
                min_sqare += 1
        
        return False
            
