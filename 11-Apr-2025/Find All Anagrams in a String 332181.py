# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = Counter(s[:len(p)-1])
        result = []
        
        left = 0
        right = len(p) -1 


        
        for right in range(len(p)-1, len(s)):
            window[s[right]]+=1
            if target == window:
                result.append(left)
            
            window[s[left]]-=1
            
            if window[s[left]] == 0:
                window.pop(s[left])
            left+=1

        return result