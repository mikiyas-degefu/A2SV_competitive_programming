# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        op = 0
        prev_num = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == prev_num:
                continue
            
            if nums[i] < prev_num:
                op += i
            
            prev_num = nums[i]
        

        return op