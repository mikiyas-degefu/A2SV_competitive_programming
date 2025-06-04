# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(idx, prev):
            if idx == len(s):
                return True 

            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if prev is None or prev - 1 == val:
                    if backtrack(i + 1, val):
                        return True
            
                if prev is not None and val >= prev:
                    break

            return False


        for i in range(len(s) - 1):
            first_val = int(s[:i+1])
            if backtrack(i + 1, first_val):
                return True

        return False