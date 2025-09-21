# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (query_row + 2) for _ in range(query_row + 2)]
        tower[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                if tower[r][c] > 1:
                    excess = (tower[r][c] - 1) / 2.0
                    tower[r+1][c] += excess
                    tower[r+1][c+1] += excess
                    tower[r][c] = 1.0 
        
        return min(1.0, tower[query_row][query_glass])