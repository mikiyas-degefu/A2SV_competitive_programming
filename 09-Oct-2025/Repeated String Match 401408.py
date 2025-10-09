# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        n = ceil(len(b) / len(a))
        
        if b in a * n:
            return n
        if b in a * (n + 1):
            return n + 1
        return -1
