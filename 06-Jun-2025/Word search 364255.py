# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COLS = len(board) , len(board[0])
        path = set()
        cur = 0

        def backtrack(i,j,cur):
            if cur == len(word):
                return True

            if (i < 0 or i >= ROW or j < 0 or j >= COLS or 
                word[cur] != board[i][j] or (i, j) in path):
                return False
            
            path.add((i, j))
            res = (
                backtrack(i + 1, j, cur + 1) or
                backtrack(i - 1, j, cur + 1) or
                backtrack(i, j + 1, cur + 1) or
                backtrack(i, j - 1, cur + 1)
            )
            path.remove((i, j))
            return res
            
            if path:
                path.pop()
            return False
        
        
        for i in range(ROW):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
                
        return False
        