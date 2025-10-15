# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dfs(l, r, score):
            if r - l + 1 < 2:
                return 0
            
            res = 0

            if nums[l] + nums[l+1] == score:
                res = max(res, 1 + dfs(l+2, r, score))

            if nums[r] + nums[r-1] == score:
                res = max(res, 1 + dfs(l, r-2, score))
  
            if nums[l] + nums[r] == score:
                res = max(res, 1 + dfs(l+1, r-1, score))
            return res
        
        ans = 0
        if n >= 2:
            ans = max(
                1 + dfs(2, n-1, nums[0] + nums[1]),   
                1 + dfs(0, n-3, nums[-2] + nums[-1]), 
                1 + dfs(1, n-2, nums[0] + nums[-1])  
            )
        return ans
