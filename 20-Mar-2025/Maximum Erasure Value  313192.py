# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique_window = set()
        max_score = 0
        window_score = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] not in unique_window:
                unique_window.add(nums[right])
                window_score+=nums[right]
                right+=1
                max_score = max(max_score, window_score)
            else:
                window_score-=nums[left]
                unique_window.remove(nums[left])
                left+=1
            
        
        return max_score

