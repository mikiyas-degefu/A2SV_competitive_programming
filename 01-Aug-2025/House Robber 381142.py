# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = defaultdict(int)

        def dp(i, robbed):
            if i >= n:
                return robbed
            
            state = (i, robbed)

            if state not in memo:
                memo[state] = max(dp(i+2, robbed + nums[i]), dp(i+1, robbed))
            
            return memo[state]
        
        return dp(0,0)