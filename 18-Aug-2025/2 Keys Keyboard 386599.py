# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        # Base case: if n is 1, we are already there in 0 steps.
        if n == 1:
            return 0

        memo = {}

        def dp(cur, copied):
            if cur > n:
                return float('inf')
            
            if cur == n:
                return 0

            if (cur, copied) in memo:
                return memo[(cur, copied)]

            paste_op = 1 + dp(cur + copied, copied)

            copy_op = float('inf')
            
            if cur != copied:
                copy_op = 1 + dp(cur, cur)
            
            memo[(cur, copied)] = min(paste_op, copy_op)
            return memo[(cur, copied)]
        
        return 1 + dp(1, 1)