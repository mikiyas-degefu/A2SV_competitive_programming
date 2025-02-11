# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices_list = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in indices_list:
                return [indices_list[diff], i]

            indices_list[num] = i

        return []

        
        