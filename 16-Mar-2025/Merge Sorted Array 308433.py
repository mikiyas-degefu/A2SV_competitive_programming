# Problem: Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx1 = m - 1
        n_idx2 = n - 1
        r = m + n - 1


        while n_idx2 >= 0:
            if m_idx1 >= 0 and nums1[m_idx1] > nums2[n_idx2]:
                nums1[r] = nums1[m_idx1]
                m_idx1-=1
            else:
                nums1[r] = nums2[n_idx2]
                n_idx2-=1
            r-=1

        