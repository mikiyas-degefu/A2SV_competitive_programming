# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        prev = 0
        patch = 0

        for num in nums:
            while num - prev > 1 and prev < n:
                patch += 1
                prev += prev + 1
            prev += num
        
        while prev < n:
            patch += 1
            prev += prev + 1
        
        return patch

            
        