# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            curSum = max(curSum, 0)
            curSum += i
            maxSum = max(maxSum, curSum)
        
        minSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = min(curSum, 0)
            curSum += num
            minSum = min(minSum, curSum)

        
        return max(abs(minSum), maxSum)
        