# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            largest_1 = - heapq.heappop(heap)
            largest_2 = - heapq.heappop(heap)

            if largest_1 != largest_2:
                heapq.heappush(heap, -(largest_1 - largest_2))

        
        return -heap[0] if heap else 0