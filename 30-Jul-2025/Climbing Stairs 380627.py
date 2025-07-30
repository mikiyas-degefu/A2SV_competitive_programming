# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        def ways(n):
            if n < 3:
                return n
            
            if memo[n]:
                return memo[n]

            memo[n] = ( ways(n-1) + ways(n-2))

            return memo[n]
        
        return ways(n)