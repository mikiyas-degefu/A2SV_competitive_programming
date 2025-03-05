# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0] * 3

        for num in nums:
            result[num]+=1
        
        idx = 0
        for index, num in enumerate(result):
            nums[idx : idx + num] = [index] * num
            idx+=num 
