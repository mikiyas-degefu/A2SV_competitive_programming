# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_moves = 0
        n = target

        while n > 1:

            if n % 2 == 0 and maxDoubles:
                maxDoubles -= 1
                n = n // 2

            elif not maxDoubles:
                return n + min_moves - 1

            else:
                n -= 1
            
            min_moves += 1
        
        return min_moves

        