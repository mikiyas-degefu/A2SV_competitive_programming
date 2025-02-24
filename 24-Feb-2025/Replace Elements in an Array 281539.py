# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

from collections import defaultdict
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_position = defaultdict(int)

        for i, val in enumerate(nums):
            nums_position[val] = i

        for i in operations:
            index_nums = nums_position[i[0]]
            nums[index_nums] = i[1]

            del nums_position[i[0]]
            nums_position[i[1]] = index_nums
        
        return nums
        
        
        