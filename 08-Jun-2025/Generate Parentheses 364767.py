# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(op, close):
            if op == n and close == n:
                res.append("".join(stack))
                return 
            
            if op < n:
                stack.append('(')
                backtrack(op + 1, close)
                stack.pop()
            if close < op:
                stack.append(')')
                backtrack(op, close + 1)
                stack.pop()
        
        
        backtrack(0,0)
        return res
        