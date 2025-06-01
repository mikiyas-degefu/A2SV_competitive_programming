# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        res = []

        for i,n in enumerate(nums):
            right_sum = total_sum - n - left_sum
            left_size = i
            right_size = len(nums) - i - 1
            res.append(
                i * n - left_sum + 
                right_sum - right_size * n
            )
            left_sum += n
        return res