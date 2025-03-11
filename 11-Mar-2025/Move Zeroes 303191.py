# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for i in range(len(nums)):
           if nums[i] != 0:
            nums[i] , nums[left] = nums[left], nums[i]
            left = left + 1


        