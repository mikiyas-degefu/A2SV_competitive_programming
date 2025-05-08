# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = 1
        right = max(nums)
        divisor = right
        while left < right:
            mid = (left + right) // 2

            prefix = 0
            for num in nums:
                prefix += (math.ceil(num / mid))
            
            if prefix > threshold:
                left = mid + 1
            else:
                divisor = mid
                right = mid
        
        return divisor

            
            
        