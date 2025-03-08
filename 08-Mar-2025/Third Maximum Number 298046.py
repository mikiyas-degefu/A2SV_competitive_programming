# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

import math
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            
            elif num < first_max and num > second_max:
                third_max = second_max
                second_max = num
    
            elif num < second_max and num > third_max:
                third_max = num

        if math.isinf(third_max):
            return first_max
        else:
            return third_max
        