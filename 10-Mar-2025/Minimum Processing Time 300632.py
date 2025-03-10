# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        tasks.sort()
        processorTime.sort(reverse = True)
        result = []

        max_num = 0
        track = 3
        i = 0
        for idx, num in enumerate(tasks):
            max_num = max(max_num, num)
            if idx == track:
                result.append(max_num + processorTime[i])
                i+=1 
                track+=4
                max_num = 0
        
        return max(result)
            
            



