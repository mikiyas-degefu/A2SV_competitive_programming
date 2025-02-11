# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = {}
        count = 0

        for i in nums1:
            for j in nums2:
                result[i+j] = result.get(i+j, 0) + 1
        
        for k in nums3:
            for l in nums4:
                if 0 - (k+l) in result:
                    count+=result[0 - (k+l)]

        return count

        

        