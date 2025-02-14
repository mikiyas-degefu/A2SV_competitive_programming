# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        start_range = left
        is_changing = False

        for i in ranges:
            if i[0] <= start_range <= i[1]:
                start_range = i[1] + 1 
                is_changing = True

        if start_range > right and is_changing:
            return True 
        return False

        