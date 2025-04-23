# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)