# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        cumulative= 0

        for num in nums:
            cumulative+=num
            result.append(cumulative)
        
        return result


        