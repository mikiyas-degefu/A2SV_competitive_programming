# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        merge = nums1[:m] + nums2[:n]

        for i in range(0,len(merge)):
            key = i
            for j in range(i+1, len(merge)):
                if merge[key] > merge[j]:
                    key = j
            
            temp = merge[i]
            merge[i] = merge[key]
            merge[key] = temp

            nums1[i] = merge[i]
       
        