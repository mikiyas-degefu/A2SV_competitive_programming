# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        indexed_tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, index = indexed_tasks[i]
                heapq.heappush(min_heap, (process, index))
                i += 1
            
            if min_heap:
                process, index = heapq.heappop(min_heap)
                time += process
                result.append(index)
            else:
                time = indexed_tasks[i][0]
        
        return result