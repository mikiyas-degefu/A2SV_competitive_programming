# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = deque()

        idx_a = len(a) - 1
        idx_b = len(b) - 1
        rem = 0

        while idx_a >= 0 or idx_b >= 0 or rem:
            op_1 = int(a[idx_a]) if idx_a >= 0 else 0
            op_2 = int(b[idx_b]) if idx_b >= 0 else 0

            cur = op_1 + op_2 + rem
            res.appendleft(str(cur % 2)) 

            rem = cur // 2

            idx_a -= 1
            idx_b -= 1
        
        return "".join(res)


                
        