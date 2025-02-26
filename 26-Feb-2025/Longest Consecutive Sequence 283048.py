# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1

                while num + length in nums_set:
                    length+=1

                longest = max(length, longest)
        
        return longest
