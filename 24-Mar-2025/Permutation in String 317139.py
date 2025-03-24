# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        windows_s2 = defaultdict(int)

        left = 0
        right = 0
        formed = 0

        if len(s1) > len(s2):
            return False
        while right < len(s1):
            if s2[right] in s1_count:
                windows_s2[s2[right]]+=1
            right+=1

        if s1_count == windows_s2:
            return True
        else:
            while right < len(s2):
                if s2[right] in s1_count:
                    windows_s2[s2[right]]+=1
                
                if s2[left] in windows_s2:
                    windows_s2[s2[left]]-=1

                if s1_count == windows_s2:
                    return True
                left+=1
                right+=1
        
        return False

