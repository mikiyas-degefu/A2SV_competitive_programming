# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int):
        results = []
        memo = {}

        def build_board(positions):
            board = []
            for i in range(n):
                row = ["." for _ in range(n)]
                row[positions[i]] = "Q"
                board.append("".join(row))
            return board

        def dp(row, cols, diag1, diag2, positions):
            state = (row, cols, diag1, diag2, positions)
            if state in memo:
                return memo[state]

            if row == n:
                results.append(build_board(positions))
                memo[state] = None
                return

            available = ((1 << n) - 1) & (~(cols | diag1 | diag2))

            while available:
                p = available & -available
                col = (p.bit_length() - 1)

                dp(row + 1,
                   cols | p,
                   (diag1 | p) << 1,
                   (diag2 | p) >> 1,
                   positions + (col,))

                available &= available - 1

            memo[state] = None  

        dp(0, 0, 0, 0, ())
        return results