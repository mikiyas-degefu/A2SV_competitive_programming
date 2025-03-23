# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_t = Counter(t)
        window_s = defaultdict(int)
        min_len = float('inf')
        min_point = []
        left = 0
        right = 0
        formed = 0

        while right < len(s):
            if s[right] in window_t:
                window_s[s[right]] += 1
                if window_s[s[right]] == window_t[s[right]]:
                    formed += 1
            
            right+=1
            while formed == len(window_t):
                if right - left < min_len:
                    min_len = right - left
                    min_point = [left, right]
                
                if s[left] in window_t:
                    window_s[s[left]] -= 1
                    if window_s[s[left]] < window_t[s[left]]:
                        formed -= 1
                
                left+=1
        
        return s[min_point[0]:min_point[1]] if min_point else ""

