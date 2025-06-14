# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_map = Counter(s)

        res = 0
        has_odd_frequency = False
        for freq in frequency_map.values():
            if (freq % 2) == 0:
                res += freq
            else:
                res += freq - 1
                has_odd_frequency = True
                
        if has_odd_frequency:
            return res + 1

        return res