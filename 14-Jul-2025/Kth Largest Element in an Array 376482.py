# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]

        heapq.heapify(heap)

        for i in range(k):
            largest = - heapq.heappop(heap)

            if i == k - 1:
                return largest
        
