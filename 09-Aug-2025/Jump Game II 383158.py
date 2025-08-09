# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = defaultdict(int)

        def dp(i):
            if i >= n - 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            max_reach = min(i + nums[i], n - 1)
            min_jumps = float('inf')

            for next_step in range(i + 1, max_reach + 1):
                min_jumps = min(min_jumps, dp(next_step) + 1)
            
            memo[i] = min_jumps
            return min_jumps
        
        return dp(0)