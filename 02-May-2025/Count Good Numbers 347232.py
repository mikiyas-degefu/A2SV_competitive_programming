# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_indices = (n + 1) // 2
        odd_indices = n //2  
        mod = (10**9) + 7 


        def power(x, y):
            if y == 0:
                return 1

            half = power(x, y // 2)
            if y % 2:
                return (x * half * half) % mod
            return (half * half) % mod


        return (power(5,even_indices) * power(4,odd_indices)) % mod
        