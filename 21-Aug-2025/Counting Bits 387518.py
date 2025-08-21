# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            count = 0
            cur = i
            while cur:
                count += (cur & 1)
                cur >>= 1
            
            res.append(count)
        
        return res
