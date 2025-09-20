# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or k == 0:
            return res

        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(len(nums1), k))]
        heapq.heapify(heap)

        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return res