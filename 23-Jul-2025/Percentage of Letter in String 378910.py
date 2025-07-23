# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        s_frq = Counter(s)

        if letter in s_frq:
            return s_frq[letter] * 100 // len(s)
        
        return 0
