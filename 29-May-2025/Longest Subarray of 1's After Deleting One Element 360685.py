# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        left = 0
        right = 0

        ones_counter = 0
        zero_counter = 0

        for right in range(len(nums)):
            if nums[right]:
                ones_counter += 1
            else:
                zero_counter += 1
            
            if zero_counter > 1:
                if nums[left] == 0:
                    zero_counter -= 1
                else:
                    ones_counter -= 1
                    
                left += 1
            res = max(res, ones_counter)
        
        if res == len(nums):
            return res - 1
        return res
        


