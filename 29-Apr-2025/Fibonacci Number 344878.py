# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        
        if n == 1: return 1
        if n == 0: return 0

        one = self.fib(n-1)
        two = self.fib(n-2)

        return one + two