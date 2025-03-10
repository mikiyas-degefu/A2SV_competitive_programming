# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_nums = sorted(intervals, key = lambda x : x[0])
        
        result = []
        start = sorted_nums[0][0]
        end = sorted_nums[0][1]

        for num in sorted_nums:
            if end < num[0]:
                result.append([start, end])
                start = num[0]

            end = max(num[1], num[0], end)
        
        result.append([start, end])
        return result