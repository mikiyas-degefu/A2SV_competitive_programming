# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

from collections import defaultdict
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 1
        last = 0
        while right < len(s):
            if s[right] == s[right - 1]:
                if last:
                    left = last
                last = right
            right+=1
            max_len = max(max_len, right - left + 1)
        return max_len - 1 if len(s) > 1 else 1


            