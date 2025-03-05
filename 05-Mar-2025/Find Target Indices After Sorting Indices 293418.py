# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for index,num in enumerate(nums):
            if num == target:
                result.append(index)
        
        return result