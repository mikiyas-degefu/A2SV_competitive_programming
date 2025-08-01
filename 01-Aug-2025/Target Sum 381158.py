# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, cur):
            if i == n:
                return 1 if cur == target else 0
            
            if (i, cur) not in memo:
                memo[(i, cur)] = dp(i + 1, cur + nums[i]) + dp(i + 1, cur - nums[i])
            
            return memo[(i, cur)]
        
        return dp(0,0)

        