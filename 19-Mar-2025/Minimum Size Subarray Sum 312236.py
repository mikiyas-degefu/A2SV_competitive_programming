# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        right = 0

        window_sum = nums[0]
        window_len = 1

        while right < len(nums) and left <= right: 
            if window_sum < target and right + 1 < len(nums):
                right+=1
                window_sum+=nums[right]
                window_len+=1
            elif window_sum >= target:
                min_len = min(min_len,window_len)
                window_sum-=nums[left]
                window_len-=1
                left+=1
            else:
                return 0 if math.isinf(min_len) else min_len
        

        return min_len


        