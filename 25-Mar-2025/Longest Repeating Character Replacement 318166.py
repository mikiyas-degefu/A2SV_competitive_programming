# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track_s = defaultdict(int)
        left = 0
        max_len = 0
        win_len = 0

        for right in range(len(s)):
            track_s[s[right]]+=1
            win_len = max(win_len, track_s[s[right]])

            if right - left + 1 - win_len > k:
                track_s[s[left]] -= 1

                if track_s[s[left]] == 0:
                    track_s.pop(s[left])
                
                left+=1
                if track_s:
                    win_len = max(track_s.values())
            max_len = max(max_len, right - left + 1)
        
        return max_len


