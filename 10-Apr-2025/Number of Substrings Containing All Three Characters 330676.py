# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        appear = {
            "a" : 0,
            "b" : 0,
            "c" : 0
        }

        left = 0
        counter = 0

        for right in range(len(s)):
            appear[s[right]] += 1

            while appear["a"] > 0 and appear["b"] > 0 and appear["c"] > 0:
                counter += len(s) - right
                appear[s[left]] -= 1
                left += 1

        return counter
                
           