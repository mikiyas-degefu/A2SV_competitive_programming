# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)

        for l,r,di in shifts:
            if di == 1:
                prefix[l] += 1
                prefix[r + 1] -= 1
            else:
                prefix[l] -= 1
                prefix[r + 1] += 1
        
        shift = 0
        result = []
        for i in range(len(s)):
            shift = (shift + prefix[i]) % 26

            if shift < 0:
                shift+=26
            
            char = chr(
                (ord(s[i]) - ord("a") + shift) % 26 + ord("a")
            )
            result.append(char)
        
        return "".join(result)
            


