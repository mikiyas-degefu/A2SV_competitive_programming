# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

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

        