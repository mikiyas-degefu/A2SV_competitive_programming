# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        expo = 0
        for num in b:
            expo += num
            expo *= 10
        expo //= 10

        def pow(x,n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                half = pow(x, n // 2) 
                return (half * half)  % 1337
            else:
                return x * pow(x, n - 1)  % 1337
        
        return pow(a,expo) % 1337