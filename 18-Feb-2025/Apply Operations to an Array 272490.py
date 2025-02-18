# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0

        result = [0] * len(nums)

        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                result[pointer] = nums[i]
                pointer+=1
        
        return result 