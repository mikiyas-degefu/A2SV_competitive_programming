# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        def heap_push(heap, value):
            heap.append(value)
            cur = len(heap) - 1
            heap_up(heap, cur)

        def heap_up(heap, cur):
            while cur > 0:
                parent = (cur - 1) // 2 
                if heap[parent] < heap[cur]:
                    heap[parent], heap[cur] = heap[cur], heap[parent]
                    cur = parent
                else:
                    break
        
        for pile in piles:
            heap_push(heap, pile)
        
        def minimize_stone(heap):
            heap[0] = math.ceil(heap[0]/2)
            heap_down(heap,0)
        
        def heap_down(heap, cur):
            while True:
                child1 = 2 * cur + 1
                child2 = 2 * cur + 2
                maximum = cur

                if child1 < len(heap) and heap[child1] > heap[maximum]:
                    maximum = child1
                
                if child2 < len(heap) and heap[child2] > heap[maximum]:
                    maximum = child2
                
                if maximum == cur:
                    break
                
                heap[cur], heap[maximum] = heap[maximum], heap[cur]
                cur = maximum

        for i in range(k):
            minimize_stone(heap)

        return sum(heap)

        
