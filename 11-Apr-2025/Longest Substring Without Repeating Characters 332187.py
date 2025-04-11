# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = {}
        left = 0
        right = 0
        max_sum = 0
        windows_sum = 0

        while right < len(s):
            if s[right] not in longest_substring:
                longest_substring[s[right]] = None
                windows_sum+=1
                max_sum = max(windows_sum,max_sum)
                right+=1
            else:
                windows_sum-=1
                longest_substring.pop(s[left])
                left+=1
        
        return max_sum