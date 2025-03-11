# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

from collections import defaultdict
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return -1

        nums.sort()
        elements = defaultdict(int)

        for num in nums:
            elements[num] = None
        
        streak = []
        count = 0
        for key,val in elements.items():
            stk = key
            has_element = False
            while stk**2 in elements:
                count+=1
                stk = stk**2
                has_element = True

            if has_element:
                streak.append(count + 1)
            count = 0

        return  max(streak) if streak else -1


