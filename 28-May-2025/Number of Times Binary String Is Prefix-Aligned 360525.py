# Problem: Number of Times Binary String Is Prefix-Aligned - https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right, res = 0, 0

        for i, num in enumerate(flips):
            right = max(right, num)
            res += right == (i + 1)
        return res
        