# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = nums[0]
        pos = 1


        for i in range(1, len(nums)):
            if unique != nums[i]:
                nums[pos] = nums[i]
                unique = nums[i]
                if pos != i:
                    nums[i] = '_'
                pos+=1
            else:
                nums[i] = '_'
        
        return pos
            


            