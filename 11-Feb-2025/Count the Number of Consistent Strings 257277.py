# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            checker = True
            for char in word:
                if char in allowed:
                    pass
                else:
                    checker = False
                    break
            
            if checker:
                count+=1

        return count


        