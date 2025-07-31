# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        length = len(nums)
        memo = defaultdict(int)

        def dp(i, target):
            if i >= length or target <= 0:
                return target == 0
            

            state = (i, target)

            if state not in memo:
                memo[state] = dp(i+1, target - nums[i]) or dp(i + 1, target)
            
            return memo[state] 
        

        return n % 2 == 0 and dp(0, n//2)
        