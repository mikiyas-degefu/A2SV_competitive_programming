# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_num = 0
        left = 0
        right = 0
        while right < k and right < len(nums):
            max_num += nums[right]
            right+=1
        
        windows_sum = max_num
        right-=1
        while right < len(nums)-1:
            windows_sum-=nums[left]
            windows_sum+=nums[right+1]
            max_num = max(max_num, windows_sum)
            left+=1
            right+=1       
        return max_num/k