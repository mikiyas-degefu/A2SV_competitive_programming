# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums):
        min_num = min(nums)
        max_num = max(nums)
        return self.gcd(min_num, max_num)

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
