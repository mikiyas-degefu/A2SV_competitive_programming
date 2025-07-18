# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_interval = sorted(intervals, key=lambda x : x[1])

        removed = 0
        prev_end = sorted_interval[0][1]

        for i in range(1, len(sorted_interval)):
            if sorted_interval[i][0] < prev_end:
                removed += 1
            else:
                prev_end = sorted_interval[i][1]
        
        return removed