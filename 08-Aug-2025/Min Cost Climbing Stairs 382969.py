# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dp(i):
            if i <= 1:
                return 0
            
            if i not in memo:
                memo[i] = min(dp(i-1) + cost[i - 1], dp(i-2) + cost [i - 2])
            
            return memo[i]

        return dp(n)