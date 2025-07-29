# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(list)

        def fib_memo(n):
            if n == 0 or n == 1:
                return n
            
            if n not in memo:
                memo[n] = fib_memo(n-1) + fib_memo(n-2)
        
            return memo[n]
        
        return fib_memo(n)
