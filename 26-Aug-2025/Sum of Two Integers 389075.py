# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        bin_a = format(a & 0xFFFFFFFF, "032b")
        bin_b = format(b & 0xFFFFFFFF, "032b")

        res = deque()
        idx_a = len(bin_a) - 1
        idx_b = len(bin_b) - 1
        rem = 0

        while idx_a >= 0 or idx_b >= 0 or rem:
            op_1 = int(bin_a[idx_a]) if idx_a >= 0 else 0
            op_2 = int(bin_b[idx_b]) if idx_b >= 0 else 0

            cur = op_1 + op_2 + rem
            res.appendleft(str(cur % 2))
            rem = cur // 2

            idx_a -= 1
            idx_b -= 1

        result_bin = "".join(res)[-32:]  
        result_int = int(result_bin, 2)

        if result_int >= (1 << 31):
            result_int -= (1 << 32)

        return result_int
