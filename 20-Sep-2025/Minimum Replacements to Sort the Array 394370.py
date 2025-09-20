# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        limit = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= limit:
                limit = nums[i]
            else:
                k = math.ceil(nums[i] / limit)
                operations += k - 1
                limit = nums[i] // k 
        return operations