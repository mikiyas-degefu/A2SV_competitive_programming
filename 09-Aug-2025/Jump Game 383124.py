# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i >= n-1:
                return True
            
            for next_step in range(i+1, min(i + nums[i], n-1) + 1):
                if dp(next_step):
                    memo[i] = True
                    return True
                    
            memo[i] = False
            return False
    
        return dp(0)