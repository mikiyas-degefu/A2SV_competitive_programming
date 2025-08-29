# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            for j in reversed(res):
                res.append(j | (1 << i))
        return res