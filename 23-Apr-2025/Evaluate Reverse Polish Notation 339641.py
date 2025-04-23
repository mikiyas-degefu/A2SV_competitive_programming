# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if (len(token) > 1 and token[0] == '-') or token.isdigit():
                stack.append(int(token))
            else:
                if len(stack) > 1:
                    v1 = stack.pop()
                    v2 = stack.pop()

                    if token == '+':
                        res = v2 + v1
                    elif token == '-':
                        res = v2 - v1
                    elif token == '/':
                        res = int(v2 / v1)
                    else:
                        res = v2 * v1

                    stack.append(res) 

        return stack[0]

        
       