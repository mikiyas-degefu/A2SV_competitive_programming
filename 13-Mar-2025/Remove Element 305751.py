# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        placer = 0
        seeker = 0

        while seeker < len(nums):
            if nums[seeker] != val:
                nums[placer] = nums[seeker]
                placer+=1
            seeker+=1
            
        return placer
        