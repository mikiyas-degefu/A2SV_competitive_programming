# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i < 0:
                return 0
                
            if i == 0:
                return nums[i]
            
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            
            return memo[i]

        return dp(n-1)