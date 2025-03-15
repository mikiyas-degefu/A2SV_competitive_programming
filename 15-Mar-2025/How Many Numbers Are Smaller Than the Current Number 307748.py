# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from collections import defaultdict
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        num_smaller = defaultdict(int)
        result = []

        for i, num in enumerate(sorted_nums):
            if num not in num_smaller:
                num_smaller[num] = i
        
        for num in nums:
            result.append(num_smaller[num])
        
        return result
        

        
