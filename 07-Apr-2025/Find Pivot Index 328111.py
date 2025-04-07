# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftSum, rightSum = 0, sum(nums)

        for i, ele in enumerate(nums):
            rightSum -= ele

            if leftSum == rightSum:
                return i
            leftSum += ele
        
        return -1