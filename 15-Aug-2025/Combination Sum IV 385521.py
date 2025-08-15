# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        def dp(cur_sum):
            if cur_sum > target:
                return 0
            if cur_sum == target:
                return 1
            if cur_sum in memo:
                return memo[cur_sum]

            total = 0
            
            for num in nums:
                total += dp(cur_sum + num)

            memo[cur_sum] = total
            return total
        
        return dp(0)
