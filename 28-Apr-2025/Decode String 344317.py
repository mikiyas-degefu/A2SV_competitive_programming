# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        k = 0

        for c in s:
            if c == "[":
                stack.append((cur_str, k))
                cur_str = ''
                k = 0
            elif c == ']':
                last_str, last_k = stack.pop()
                cur_str = last_str + last_k * cur_str
            
            elif c.isdigit():
                k = k * 10 + int(c)
            
            else:
                cur_str += c
        
        return cur_str