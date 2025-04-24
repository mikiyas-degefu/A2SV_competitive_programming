# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s):
        brackets = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char not in pairs:
                brackets.append(char)
            elif not brackets or brackets[-1] != pairs[char]:
                return False
            else:
                brackets.pop()
                
        return len(brackets) == 0